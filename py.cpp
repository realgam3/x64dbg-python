#include "py.h"
#include "stringutils.h"
#include <windows.h>
#include <stdio.h>
#include <psapi.h>
#include <python.h>
#include <shlwapi.h>

#pragma comment(lib, "shlwapi.lib")

#define module_name "x64dbg_python"
#define event_object_name "Event"
#define autorun_directory L"plugins\\x64dbg_python\\autorun"

PyObject* pModule, *pEventObject;

extern "C" __declspec(dllexport) void CBMENUENTRY(CBTYPE cbType, PLUG_CB_MENUENTRY* info)
{
    switch(info->hEntry)
    {
    case MENU_OPEN:
        DbgCmdExec("OpenScript");
        break;

    case MENU_ABOUT:
        MessageBoxA(hwndDlg, "Made By RealGame(Tomer Zait)", plugin_name " Plugin", MB_ICONINFORMATION);
        break;
    }
}

static bool cbPythonCommand(int argc, char* argv[])
{
    if(argc < 2)
    {
        _plugin_logputs("[PYTHON] Command Example: Python \"print('Hello World')\".");
        return false;
    }
    PyRun_SimpleString(argv[1]);
    return true;
}

static bool OpenFileDialog(wchar_t Buffer[MAX_PATH])
{
    OPENFILENAMEW sOpenFileName = {0};
    const wchar_t szFilterString[] = L"Python files\0*.py\0\0";
    const wchar_t szDialogTitle[] = L"Select script file...";
    sOpenFileName.lStructSize = sizeof(sOpenFileName);
    sOpenFileName.lpstrFilter = szFilterString;
    sOpenFileName.nFilterIndex = 1;
    sOpenFileName.lpstrFile = Buffer;
    sOpenFileName.nMaxFile = MAX_PATH;
    sOpenFileName.Flags = OFN_PATHMUSTEXIST | OFN_FILEMUSTEXIST;
    sOpenFileName.lpstrTitle = szDialogTitle;
    sOpenFileName.hwndOwner = GuiGetWindowHandle();
    return (FALSE != GetOpenFileNameW(&sOpenFileName));
}

static bool ExecutePythonScript(wchar_t* szFileName)
{
    int status_code;
    String szFileNameA = Utf16ToUtf8(szFileName);
    PyObject* PyFileObject = PyFile_FromString((char*)szFileNameA.c_str(), "r");
    if(PyFileObject == NULL)
    {
        _plugin_logputs("[PYTHON] Could not open file....");
        return false;
    }

    status_code = PyRun_SimpleFile(PyFile_AsFile(PyFileObject), (char*)szFileNameA.c_str());
    Py_DECREF(PyFileObject);
    if(status_code != EXIT_SUCCESS)
    {
        _plugin_logprintf("[PYTHON] Execution failed (status code: %d)....\n", status_code);
        return false;
    }

    _plugin_logputs("[PYTHON] Execution is done!");
    return true;
}

// OpenScript [EntryPointVA]
static bool cbOpenScriptCommand(int argc, char* argv[])
{
    wchar_t szFileName[MAX_PATH] = {0};
    if(!OpenFileDialog(szFileName))
        return false;

    return ExecutePythonScript(szFileName);
}

static void cbWinEventCallback(CBTYPE cbType, void* info)
{
    MSG* msg = ((PLUG_CB_WINEVENT*)info)->message;
    switch(msg->message)
    {
    case WM_HOTKEY:
        // Hotkeys
        switch(msg->wParam)
        {
        case 1:
            cbOpenScriptCommand(NULL, NULL);
            break;
        }
        break;
    }
}

static void cbInitDebugCallback(CBTYPE cbType, void* info)
{
    WIN32_FIND_DATAW FindFileData;
    HANDLE hFind = INVALID_HANDLE_VALUE;
    wchar_t autorunDirectory[MAX_PATH], currentDirectory[MAX_PATH];

    // Get Autorun Folder Path
    GetModuleFileNameW(NULL, autorunDirectory, MAX_PATH);
    PathRemoveFileSpecW(autorunDirectory);
    PathAppendW(autorunDirectory, autorun_directory);

    // Get Current Directory
    GetCurrentDirectoryW(MAX_PATH, currentDirectory);

    // Find And Execute *.py Files
    SetCurrentDirectoryW(autorunDirectory);
    hFind = FindFirstFileW(L"*.py", &FindFileData);
    if(hFind != INVALID_HANDLE_VALUE)
    {
        do
        {
            _plugin_logprintf("[PYTHON] Executing autorun file: '%ws'.\n", FindFileData.cFileName);
            ExecutePythonScript(FindFileData.cFileName);
        }
        while(FindNextFileW(hFind, &FindFileData) != 0);
        FindClose(hFind);
    }

    // Reset Current Directory
    SetCurrentDirectoryW(currentDirectory);
}

static void cbBreakPointCallback(CBTYPE cbType, void* info)
{
    PyObject* pFunc;
    PyObject* pArgs, *pValue;
    BRIDGEBP* breakpoint = ((PLUG_CB_BREAKPOINT*)info)->breakpoint;

    // Check if event object exist.
    if(pEventObject == NULL)
        return;

    pFunc = PyObject_GetAttrString(pEventObject, "breakpoint");
    if(pFunc && PyCallable_Check(pFunc))
    {
        pArgs = PyTuple_New(8);
        PyTuple_SetItem(pArgs, 0, PyBool_FromLong(breakpoint->active));
        PyTuple_SetItem(pArgs, 1, PyInt_FromSize_t(breakpoint->addr));
        PyTuple_SetItem(pArgs, 2, PyBool_FromLong(breakpoint->enabled));
        PyTuple_SetItem(pArgs, 3, PyString_FromString(breakpoint->mod));
        PyTuple_SetItem(pArgs, 4, PyString_FromString(breakpoint->name));
        PyTuple_SetItem(pArgs, 5, PyBool_FromLong(breakpoint->singleshoot));
        PyTuple_SetItem(pArgs, 6, PyInt_FromLong(breakpoint->slot));
        PyTuple_SetItem(pArgs, 7, PyInt_FromLong(breakpoint->type));

        pValue = PyObject_CallObject(pFunc, pArgs);
        Py_DECREF(pArgs);
        Py_DECREF(pFunc);
        if(pValue == NULL)
        {
            _plugin_logputs("[PYTHON] Could not use breakpoint function.");
            return;
        }

        Py_DECREF(pValue);
    }
}

static void cbStopDebugCallback(CBTYPE cbType, void* info)
{
    PyObject* pFunc;
    PyObject* pArgs, *pValue;

    // Check if event object exist.
    if(pEventObject == NULL)
        return;

    pFunc = PyObject_GetAttrString(pEventObject, "stop_debug");
    if(pFunc && PyCallable_Check(pFunc))
    {
        pValue = PyObject_CallObject(pFunc, NULL);
        Py_DECREF(pFunc);
        if(pValue == NULL)
        {
            _plugin_logputs("[PYTHON] Could not use stop_debug function.");
            return;
        }
        Py_DECREF(pValue);
    }
}

void pyInit(PLUG_INITSTRUCT* initStruct)
{
    _plugin_logprintf("[PYTHON] pluginHandle: %d\n", pluginHandle);
    if(!_plugin_registercommand(pluginHandle, "Python", cbPythonCommand, false))
        _plugin_logputs("[PYTHON] error registering the \"Python\" command!");
    if(!_plugin_registercommand(pluginHandle, "OpenScript", cbOpenScriptCommand, false))
        _plugin_logputs("[PYTHON] error registering the \"OpenScript\" command!");

    // Initialize the python environment
    Py_Initialize();
    PyEval_InitThreads();

    // Import x64dbg_python
    pModule = PyImport_Import(PyString_FromString(module_name));
    if(pModule != NULL)
    {
        // Get Event Object
        pEventObject = PyObject_GetAttrString(pModule, event_object_name);
        if(pEventObject == NULL)
            _plugin_logputs("[PYTHON] Could not find Event object.");
    }
    else
        _plugin_logputs("[PYTHON] Could not import " module_name ".");

    PyRun_SimpleString("from " module_name " import *\n");
}

void pyStop()
{
    _plugin_unregistercommand(pluginHandle, "Python");
    _plugin_unregistercommand(pluginHandle, "OpenScript");

    _plugin_menuclear(hMenu);
    _plugin_menuclear(hMenuDisasm);
    _plugin_menuclear(hMenuDump);
    _plugin_menuclear(hMenuStack);

    _plugin_unregistercallback(pluginHandle, CB_WINEVENT);
    _plugin_unregistercallback(pluginHandle, CB_INITDEBUG);
    _plugin_unregistercallback(pluginHandle, CB_BREAKPOINT);
    _plugin_unregistercallback(pluginHandle, CB_STOPDEBUG);

    // Properly ends the python environment
    Py_Finalize();
}

void pySetup()
{
    _plugin_menuaddentry(hMenu, MENU_OPEN, "&OpenScript...\tALT+F7");
    _plugin_menuaddentry(hMenu, MENU_ABOUT, "&About");

    // Set HotKey
    if(RegisterHotKey(hwndDlg, 1, MOD_ALT | MOD_NOREPEAT, VK_F7))
        _plugin_logputs("[PYTHON] ALT+F7 HetKey Registered To OpenScript!");

    // Set Callbacks
    _plugin_registercallback(pluginHandle, CB_WINEVENT, cbWinEventCallback);
    _plugin_registercallback(pluginHandle, CB_INITDEBUG, cbInitDebugCallback);
    _plugin_registercallback(pluginHandle, CB_BREAKPOINT, cbBreakPointCallback);
    _plugin_registercallback(pluginHandle, CB_STOPDEBUG, cbStopDebugCallback);
}

#include "py.h"
#include "pluginmain.h"
#include <windows.h>
#include <stdio.h>
#include <psapi.h>
#include <python.h>
#include <shlwapi.h>

#pragma comment(lib, "shlwapi.lib")

#define module_name "x64dbg_python"
#define event_object_name "Event"
#define autorun_directory "plugins\\" module_name "\\autorun"


PyObject* pModule, *pEventObject;

extern "C" __declspec(dllexport) void CBMENUENTRY(CBTYPE cbType, PLUG_CB_MENUENTRY* info)
{
    switch(info->hEntry)
    {
    case MENU_OPEN:
        DbgCmdExec("OpenScript");
        break;

    case MENU_ABOUT:
        MessageBoxA(hwndDlg, "Made By RealGame(Tomer Zait)", "x64dbg-python Plugin", MB_ICONINFORMATION);
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

static bool OpenFileDialog(char Buffer[MAX_PATH])
{
    OPENFILENAMEA sOpenFileName = {0};
    const char szFilterString[] = "Python files\0*.py\0\0";
    const char szDialogTitle[] = "Select script file...";
    sOpenFileName.lStructSize = sizeof(sOpenFileName);
    sOpenFileName.lpstrFilter = szFilterString;
    sOpenFileName.nFilterIndex = 1;
    sOpenFileName.lpstrFile = Buffer;
    sOpenFileName.nMaxFile = MAX_PATH;
    sOpenFileName.Flags = OFN_PATHMUSTEXIST | OFN_FILEMUSTEXIST;
    sOpenFileName.lpstrTitle = szDialogTitle;
    sOpenFileName.hwndOwner = GuiGetWindowHandle();
    return (FALSE != GetOpenFileNameA(&sOpenFileName));
}

static bool ExecutePythonScript(char* szFileName)
{
    int status_code;
    PyObject* PyFileObject = PyFile_FromString(szFileName, "r");
    if(PyFileObject == NULL)
    {
        _plugin_logputs("[PYTHON] Could not open file....");
        return false;
    }

    status_code = PyRun_SimpleFile(PyFile_AsFile(PyFileObject), szFileName);
    Py_DECREF(PyFileObject);
    if(status_code != EXIT_SUCCESS)
    {
        _plugin_logprintf("[PYTHON] Execution failed (status code: %d)....\n", status_code);
        return false;
    }

    _plugin_logputs("[PYTHON] Execution is done!");
    return true;
}

//OpenScript [EntryPointVA]
static bool cbOpenScriptCommand(int argc, char* argv[])
{
    char szFileName[MAX_PATH] = "";
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

//static void cbInitDebugEventCallback(CBTYPE cbType, void* info)
//{
//  PyObject *pFunc;
//  PyObject *szFileName, *pArgs, *pValue;
//
//  // Check if event object exist.
//  if (pEventObject == NULL)
//      return;
//
//  szFileName = PyString_FromString(((PLUG_CB_INITDEBUG*)info)->szFileName);
//  pFunc = PyObject_GetAttrString(pEventObject, "init_debug");
//  if (pFunc && PyCallable_Check(pFunc))
//  {
//      pArgs = PyTuple_New(1);
//      PyTuple_SetItem(pArgs, 0, szFileName);
//      pValue = PyObject_CallObject(pFunc, pArgs);
//      Py_DECREF(szFileName);
//      Py_DECREF(pArgs);
//      Py_DECREF(pFunc);
//      return;
//  }
//  _plugin_logputs("[PYTHON] Could not use init_debug function.");
//}

static void cbInitDebugEventCallback(CBTYPE cbType, void* info)
{
    WIN32_FIND_DATA FindFileData;
    HANDLE hFind = INVALID_HANDLE_VALUE;
    char autorunDirectory[MAX_PATH], temp[MAX_PATH];

    // Get Autorun Folder Path
    GetModuleFileNameA(NULL, autorunDirectory, MAX_PATH);
    PathRemoveFileSpecA(autorunDirectory);
    PathAppendA(autorunDirectory, autorun_directory);

    // Find And Execute *.py Files
    hFind = FindFirstFile(PathCombineA(temp, autorunDirectory, "*.py"), &FindFileData);
    if(hFind != INVALID_HANDLE_VALUE)
    {
        do
        {
            _plugin_logprintf("[PYTHON] Executing autorun file: '%s'.\n", FindFileData.cFileName);
            ExecutePythonScript(PathCombineA(temp, autorunDirectory, FindFileData.cFileName));
        }
        while(FindNextFile(hFind, &FindFileData) != 0);
        FindClose(hFind);
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
        _plugin_logputs("[PYTHON] Could not import x64dbg_python.");

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
    _plugin_registercallback(pluginHandle, CB_WINEVENT, cbWinEventCallback);
    _plugin_registercallback(pluginHandle, CB_INITDEBUG, cbInitDebugEventCallback);
}

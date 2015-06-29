#include "py.h"
#include <windows.h>
#include <stdio.h>
#include <psapi.h>
#include <python.h>

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

//OpenScript [EntryPointVA]
static bool cbOpenScriptCommand(int argc, char* argv[])
{
    char szFileName[MAX_PATH] = "";
    if(!OpenFileDialog(szFileName))
        return true;

    PyObject* PyFileObject = PyFile_FromString(szFileName, "r");
    if(PyFileObject == NULL)
    {
        _plugin_logputs("[PYTHON] Could not open file....");
        return false;
    }
    if(PyRun_SimpleFile(PyFile_AsFile(PyFileObject), szFileName) != EXIT_SUCCESS)
    {
        _plugin_logputs("[PYTHON] Could not run script....");
        return false;
    }
    _plugin_logputs("[PYTHON] Execution is done!");
    return true;
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
    PyRun_SimpleString("from x64dbg_python import *\n");
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
}

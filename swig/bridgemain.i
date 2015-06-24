%module bridgemain
%{
#include "bridgemain.h"
%}

// Allow Python Buffers
%include <pybuffer.i>

// Type Maps
%pybuffer_string(char* text);

%typemap(out) HWND {
    $result = PyInt_FromLong((long)$1);
}

#ifdef _WIN64
typedef unsigned long long duint;
typedef signed long long dsint;
#else
typedef unsigned long duint;
typedef signed long dsint;
#endif //_WIN64

%include <windows.i>
#ifndef BRIDGE_IMPEXP
#ifdef BUILD_BRIDGE
#define BRIDGE_IMPEXP __declspec(dllexport)
#else
#define BRIDGE_IMPEXP __declspec(dllimport)
#endif //BUILD_BRIDGE
#endif //BRIDGE_IMPEXP

//Bridge functions
BRIDGE_IMPEXP const char* BridgeInit();
BRIDGE_IMPEXP const char* BridgeStart();
BRIDGE_IMPEXP void* BridgeAlloc(size_t size);
BRIDGE_IMPEXP void BridgeFree(void* ptr);
BRIDGE_IMPEXP bool BridgeSettingGet(const char* section, const char* key, char* value);
BRIDGE_IMPEXP bool BridgeSettingGetUint(const char* section, const char* key, duint* value);
BRIDGE_IMPEXP bool BridgeSettingSet(const char* section, const char* key, const char* value);
BRIDGE_IMPEXP bool BridgeSettingSetUint(const char* section, const char* key, duint value);
BRIDGE_IMPEXP int BridgeGetDbgVersion();

//Debugger functions
BRIDGE_IMPEXP const char* DbgInit();
BRIDGE_IMPEXP void DbgExit();
BRIDGE_IMPEXP bool DbgMemRead(duint va, unsigned char* dest, duint size);
BRIDGE_IMPEXP bool DbgMemWrite(duint va, const unsigned char* src, duint size);
BRIDGE_IMPEXP duint DbgMemGetPageSize(duint base);
BRIDGE_IMPEXP duint DbgMemFindBaseAddr(duint addr, duint* size);
BRIDGE_IMPEXP bool DbgCmdExec(const char* cmd);
BRIDGE_IMPEXP bool DbgCmdExecDirect(const char* cmd);
BRIDGE_IMPEXP bool DbgMemMap(MEMMAP* memmap);
BRIDGE_IMPEXP bool DbgIsValidExpression(const char* expression);
BRIDGE_IMPEXP bool DbgIsDebugging();
BRIDGE_IMPEXP bool DbgIsJumpGoingToExecute(duint addr);
BRIDGE_IMPEXP bool DbgGetLabelAt(duint addr, SEGMENTREG segment, char* text);
BRIDGE_IMPEXP bool DbgSetLabelAt(duint addr, const char* text);
BRIDGE_IMPEXP bool DbgGetCommentAt(duint addr, char* text);
BRIDGE_IMPEXP bool DbgSetCommentAt(duint addr, const char* text);
BRIDGE_IMPEXP bool DbgGetBookmarkAt(duint addr);
BRIDGE_IMPEXP bool DbgSetBookmarkAt(duint addr, bool isbookmark);
BRIDGE_IMPEXP bool DbgGetModuleAt(duint addr, char* text);
BRIDGE_IMPEXP BPXTYPE DbgGetBpxTypeAt(duint addr);
BRIDGE_IMPEXP duint DbgValFromString(const char* string);
BRIDGE_IMPEXP bool DbgGetRegDump(REGDUMP* regdump);
BRIDGE_IMPEXP bool DbgValToString(const char* string, duint value);
BRIDGE_IMPEXP bool DbgMemIsValidReadPtr(duint addr);
BRIDGE_IMPEXP int DbgGetBpList(BPXTYPE type, BPMAP* list);
BRIDGE_IMPEXP FUNCTYPE DbgGetFunctionTypeAt(duint addr);
BRIDGE_IMPEXP LOOPTYPE DbgGetLoopTypeAt(duint addr, int depth);
BRIDGE_IMPEXP duint DbgGetBranchDestination(duint addr);
BRIDGE_IMPEXP void DbgScriptLoad(const char* filename);
BRIDGE_IMPEXP void DbgScriptUnload();
BRIDGE_IMPEXP void DbgScriptRun(int destline);
BRIDGE_IMPEXP void DbgScriptStep();
BRIDGE_IMPEXP bool DbgScriptBpToggle(int line);
BRIDGE_IMPEXP bool DbgScriptBpGet(int line);
BRIDGE_IMPEXP bool DbgScriptCmdExec(const char* command);
BRIDGE_IMPEXP void DbgScriptAbort();
BRIDGE_IMPEXP SCRIPTLINETYPE DbgScriptGetLineType(int line);
BRIDGE_IMPEXP void DbgScriptSetIp(int line);
BRIDGE_IMPEXP bool DbgScriptGetBranchInfo(int line, SCRIPTBRANCH* info);
BRIDGE_IMPEXP void DbgSymbolEnum(duint base, CBSYMBOLENUM cbSymbolEnum, void* user);
BRIDGE_IMPEXP bool DbgAssembleAt(duint addr, const char* instruction);
BRIDGE_IMPEXP duint DbgModBaseFromName(const char* name);
BRIDGE_IMPEXP void DbgDisasmAt(duint addr, DISASM_INSTR* instr);
BRIDGE_IMPEXP bool DbgStackCommentGet(duint addr, STACK_COMMENT* comment);
BRIDGE_IMPEXP void DbgGetThreadList(THREADLIST* list);
BRIDGE_IMPEXP void DbgSettingsUpdated();
BRIDGE_IMPEXP void DbgDisasmFastAt(duint addr, BASIC_INSTRUCTION_INFO* basicinfo);
BRIDGE_IMPEXP void DbgMenuEntryClicked(int hEntry);
BRIDGE_IMPEXP bool DbgFunctionGet(duint addr, duint* start, duint* end);
BRIDGE_IMPEXP bool DbgFunctionOverlaps(duint start, duint end);
BRIDGE_IMPEXP bool DbgFunctionAdd(duint start, duint end);
BRIDGE_IMPEXP bool DbgFunctionDel(duint addr);
BRIDGE_IMPEXP bool DbgLoopGet(int depth, duint addr, duint* start, duint* end);
BRIDGE_IMPEXP bool DbgLoopOverlaps(int depth, duint start, duint end);
BRIDGE_IMPEXP bool DbgLoopAdd(duint start, duint end);
BRIDGE_IMPEXP bool DbgLoopDel(int depth, duint addr);
BRIDGE_IMPEXP bool DbgIsRunLocked();
BRIDGE_IMPEXP bool DbgIsBpDisabled(duint addr);
BRIDGE_IMPEXP bool DbgSetAutoCommentAt(duint addr, const char* text);
BRIDGE_IMPEXP void DbgClearAutoCommentRange(duint start, duint end);
BRIDGE_IMPEXP bool DbgSetAutoLabelAt(duint addr, const char* text);
BRIDGE_IMPEXP void DbgClearAutoLabelRange(duint start, duint end);
BRIDGE_IMPEXP bool DbgSetAutoBookmarkAt(duint addr);
BRIDGE_IMPEXP void DbgClearAutoBookmarkRange(duint start, duint end);
BRIDGE_IMPEXP bool DbgSetAutoFunctionAt(duint start, duint end);
BRIDGE_IMPEXP void DbgClearAutoFunctionRange(duint start, duint end);
BRIDGE_IMPEXP bool DbgGetStringAt(duint addr, char* text);
BRIDGE_IMPEXP const DBGFUNCTIONS* DbgFunctions();
BRIDGE_IMPEXP bool DbgWinEvent(MSG* message, long* result);
BRIDGE_IMPEXP bool DbgWinEventGlobal(MSG* message);
BRIDGE_IMPEXP bool DbgIsRunning();

//GUI functions
BRIDGE_IMPEXP void GuiDisasmAt(duint addr, duint cip);
BRIDGE_IMPEXP void GuiSetDebugState(DBGSTATE state);
BRIDGE_IMPEXP void GuiAddLogMessage(const char* msg);
BRIDGE_IMPEXP void GuiLogClear();
BRIDGE_IMPEXP void GuiUpdateAllViews();
BRIDGE_IMPEXP void GuiUpdateRegisterView();
BRIDGE_IMPEXP void GuiUpdateDisassemblyView();
BRIDGE_IMPEXP void GuiUpdateBreakpointsView();
BRIDGE_IMPEXP void GuiUpdateWindowTitle(const char* filename);
BRIDGE_IMPEXP HWND GuiGetWindowHandle();
BRIDGE_IMPEXP void GuiDumpAt(duint va);
BRIDGE_IMPEXP void GuiScriptAdd(int count, const char** lines);
BRIDGE_IMPEXP void GuiScriptClear();
BRIDGE_IMPEXP void GuiScriptSetIp(int line);
BRIDGE_IMPEXP void GuiScriptError(int line, const char* message);
BRIDGE_IMPEXP void GuiScriptSetTitle(const char* title);
BRIDGE_IMPEXP void GuiScriptSetInfoLine(int line, const char* info);
BRIDGE_IMPEXP void GuiScriptMessage(const char* message);
BRIDGE_IMPEXP int GuiScriptMsgyn(const char* message);
BRIDGE_IMPEXP void GuiScriptEnableHighlighting(bool enable);
BRIDGE_IMPEXP void GuiSymbolLogAdd(const char* message);
BRIDGE_IMPEXP void GuiSymbolLogClear();
BRIDGE_IMPEXP void GuiSymbolSetProgress(int percent);
BRIDGE_IMPEXP void GuiSymbolUpdateModuleList(int count, SYMBOLMODULEINFO* modules);
BRIDGE_IMPEXP void GuiSymbolRefreshCurrent();
BRIDGE_IMPEXP void GuiReferenceAddColumn(int width, const char* title);
BRIDGE_IMPEXP void GuiReferenceSetRowCount(int count);
BRIDGE_IMPEXP int GuiReferenceGetRowCount();
BRIDGE_IMPEXP void GuiReferenceDeleteAllColumns();
BRIDGE_IMPEXP void GuiReferenceInitialize(const char* name);
BRIDGE_IMPEXP void GuiReferenceSetCellContent(int row, int col, const char* str);
BRIDGE_IMPEXP const char* GuiReferenceGetCellContent(int row, int col);
BRIDGE_IMPEXP void GuiReferenceReloadData();
BRIDGE_IMPEXP void GuiReferenceSetSingleSelection(int index, bool scroll);
BRIDGE_IMPEXP void GuiReferenceSetProgress(int progress);
BRIDGE_IMPEXP void GuiReferenceSetSearchStartCol(int col);
BRIDGE_IMPEXP void GuiStackDumpAt(duint addr, duint csp);
BRIDGE_IMPEXP void GuiUpdateDumpView();
BRIDGE_IMPEXP void GuiUpdateThreadView();
BRIDGE_IMPEXP void GuiUpdateMemoryView();
BRIDGE_IMPEXP void GuiAddRecentFile(const char* file);
BRIDGE_IMPEXP void GuiSetLastException(unsigned int exception);
BRIDGE_IMPEXP bool GuiGetDisassembly(duint addr, char* text);
BRIDGE_IMPEXP int GuiMenuAdd(int hMenu, const char* title);
BRIDGE_IMPEXP int GuiMenuAddEntry(int hMenu, const char* title);
BRIDGE_IMPEXP void GuiMenuAddSeparator(int hMenu);
BRIDGE_IMPEXP void GuiMenuClear(int hMenu);
BRIDGE_IMPEXP bool GuiSelectionGet(int hWindow, SELECTIONDATA* selection);
BRIDGE_IMPEXP bool GuiSelectionSet(int hWindow, const SELECTIONDATA* selection);
BRIDGE_IMPEXP bool GuiGetLineWindow(const char* title, char* text);
BRIDGE_IMPEXP void GuiAutoCompleteAddCmd(const char* cmd);
BRIDGE_IMPEXP void GuiAutoCompleteDelCmd(const char* cmd);
BRIDGE_IMPEXP void GuiAutoCompleteClearAll();
BRIDGE_IMPEXP void GuiAddStatusBarMessage(const char* msg);
BRIDGE_IMPEXP void GuiUpdateSideBar();
BRIDGE_IMPEXP void GuiRepaintTableView();
BRIDGE_IMPEXP void GuiUpdatePatches();
BRIDGE_IMPEXP void GuiUpdateCallStack();
BRIDGE_IMPEXP void GuiUpdateMemoryView();
BRIDGE_IMPEXP void GuiLoadSourceFile(const char* path, int line);
BRIDGE_IMPEXP void GuiMenuSetIcon(int hMenu, const ICONDATA* icon);
BRIDGE_IMPEXP void GuiMenuSetEntryIcon(int hEntry, const ICONDATA* icon);
BRIDGE_IMPEXP void GuiShowCpu();

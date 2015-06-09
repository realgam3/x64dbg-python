%module bridgemain
%{
#include "bridgemain.h"
%}

// Allow Python Buffers
%include <pybuffer.i>

//Debugger functions
// extern const char* DbgInit();
// extern void DbgExit();
extern bool DbgMemRead(duint va, unsigned char* dest, duint size);
extern bool DbgMemWrite(duint va, const unsigned char* src, duint size);
extern duint DbgMemGetPageSize(duint base);
extern duint DbgMemFindBaseAddr(duint addr, duint* size);
extern bool DbgCmdExec(const char* cmd);
extern bool DbgCmdExecDirect(const char* cmd);
// extern bool DbgMemMap(MEMMAP* memmap);
extern bool DbgIsValidExpression(const char* expression);
extern bool DbgIsDebugging();
extern bool DbgIsJumpGoingToExecute(duint addr);
// extern bool DbgGetLabelAt(duint addr, SEGMENTREG segment, char* text);
extern bool DbgSetLabelAt(duint addr, const char* text);

%pybuffer_string(char* text);
extern bool DbgGetCommentAt(duint addr, char* text);

extern bool DbgSetCommentAt(duint addr, const char* text);
extern bool DbgGetBookmarkAt(duint addr);
extern bool DbgSetBookmarkAt(duint addr, bool isbookmark);

%pybuffer_string(char* text);
extern bool DbgGetModuleAt(duint addr, char* text);

// extern BPXTYPE DbgGetBpxTypeAt(duint addr);
extern duint DbgValFromString(const char* string);
// extern bool DbgGetRegDump(REGDUMP* regdump);
extern bool DbgValToString(const char* string, duint value);
extern bool DbgMemIsValidReadPtr(duint addr);
// extern int DbgGetBpList(BPXTYPE type, BPMAP* list);
// extern FUNCTYPE DbgGetFunctionTypeAt(duint addr);
// extern LOOPTYPE DbgGetLoopTypeAt(duint addr, int depth);
extern duint DbgGetBranchDestination(duint addr);
extern void DbgScriptLoad(const char* filename);
extern void DbgScriptUnload();
extern void DbgScriptRun(int destline);
extern void DbgScriptStep();
extern bool DbgScriptBpToggle(int line);
extern bool DbgScriptBpGet(int line);
extern bool DbgScriptCmdExec(const char* command);
extern void DbgScriptAbort();
// extern SCRIPTLINETYPE DbgScriptGetLineType(int line);
extern void DbgScriptSetIp(int line);
// extern bool DbgScriptGetBranchInfo(int line, SCRIPTBRANCH* info);
// extern void DbgSymbolEnum(duint base, CBSYMBOLENUM cbSymbolEnum, void* user);
extern bool DbgAssembleAt(duint addr, const char* instruction);
extern duint DbgModBaseFromName(const char* name);
// extern void DbgDisasmAt(duint addr, DISASM_INSTR* instr);
// extern bool DbgStackCommentGet(duint addr, STACK_COMMENT* comment);
// extern void DbgGetThreadList(THREADLIST* list);
extern void DbgSettingsUpdated();
// extern void DbgDisasmFastAt(duint addr, BASIC_INSTRUCTION_INFO* basicinfo);
extern void DbgMenuEntryClicked(int hEntry);
extern bool DbgFunctionGet(duint addr, duint* start, duint* end);
extern bool DbgFunctionOverlaps(duint start, duint end);
extern bool DbgFunctionAdd(duint start, duint end);
extern bool DbgFunctionDel(duint addr);
extern bool DbgLoopGet(int depth, duint addr, duint* start, duint* end);
extern bool DbgLoopOverlaps(int depth, duint start, duint end);
extern bool DbgLoopAdd(duint start, duint end);
extern bool DbgLoopDel(int depth, duint addr);
extern bool DbgIsRunLocked();
extern bool DbgIsBpDisabled(duint addr);
extern bool DbgSetAutoCommentAt(duint addr, const char* text);
extern void DbgClearAutoCommentRange(duint start, duint end);
extern bool DbgSetAutoLabelAt(duint addr, const char* text);
extern void DbgClearAutoLabelRange(duint start, duint end);
extern bool DbgSetAutoBookmarkAt(duint addr);
extern void DbgClearAutoBookmarkRange(duint start, duint end);
extern bool DbgSetAutoFunctionAt(duint start, duint end);
extern void DbgClearAutoFunctionRange(duint start, duint end);

%pybuffer_string(char* text);
extern bool DbgGetStringAt(duint addr, char* text);

// extern const DBGFUNCTIONS* DbgFunctions();
// extern bool DbgWinEvent(MSG* message, long* result);
// extern bool DbgWinEventGlobal(MSG* message);


//GUI functions
extern void GuiDisasmAt(duint addr, duint cip);
// extern void GuiSetDebugState(DBGSTATE state);
extern void GuiAddLogMessage(const char* msg);
extern void GuiLogClear();
extern void GuiUpdateAllViews();
extern void GuiUpdateRegisterView();
extern void GuiUpdateDisassemblyView();
extern void GuiUpdateBreakpointsView();
extern void GuiUpdateWindowTitle(const char* filename);
extern HWND GuiGetWindowHandle();
extern void GuiDumpAt(duint va);
extern void GuiScriptAdd(int count, const char** lines);
extern void GuiScriptClear();
extern void GuiScriptSetIp(int line);
extern void GuiScriptError(int line, const char* message);
extern void GuiScriptSetTitle(const char* title);
extern void GuiScriptSetInfoLine(int line, const char* info);
extern void GuiScriptMessage(const char* message);
extern int GuiScriptMsgyn(const char* message);
extern void GuiScriptEnableHighlighting(bool enable);
extern void GuiSymbolLogAdd(const char* message);
extern void GuiSymbolLogClear();
extern void GuiSymbolSetProgress(int percent);
// extern void GuiSymbolUpdateModuleList(int count, SYMBOLMODULEINFO* modules);
extern void GuiSymbolRefreshCurrent();
extern void GuiReferenceAddColumn(int width, const char* title);
extern void GuiReferenceSetRowCount(int count);
extern int GuiReferenceGetRowCount();
extern void GuiReferenceDeleteAllColumns();
extern void GuiReferenceInitialize(const char* name);
extern void GuiReferenceSetCellContent(int row, int col, const char* str);
extern const char* GuiReferenceGetCellContent(int row, int col);
extern void GuiReferenceReloadData();
extern void GuiReferenceSetSingleSelection(int index, bool scroll);
extern void GuiReferenceSetProgress(int progress);
extern void GuiReferenceSetSearchStartCol(int col);
extern void GuiStackDumpAt(duint addr, duint csp);
extern void GuiUpdateDumpView();
extern void GuiUpdateThreadView();
extern void GuiUpdateMemoryView();
extern void GuiAddRecentFile(const char* file);
extern void GuiSetLastException(unsigned int exception);
extern bool GuiGetDisassembly(duint addr, char* text);
extern int GuiMenuAdd(int hMenu, const char* title);
extern int GuiMenuAddEntry(int hMenu, const char* title);
extern void GuiMenuAddSeparator(int hMenu);
extern void GuiMenuClear(int hMenu);
// extern bool GuiSelectionGet(int hWindow, SELECTIONDATA* selection);
// extern bool GuiSelectionSet(int hWindow, const SELECTIONDATA* selection);

%pybuffer_string(char* text);
extern bool GuiGetLineWindow(const char* title, char* text);

extern void GuiAutoCompleteAddCmd(const char* cmd);
extern void GuiAutoCompleteDelCmd(const char* cmd);
extern void GuiAutoCompleteClearAll();
extern void GuiAddStatusBarMessage(const char* msg);
extern void GuiUpdateSideBar();
extern void GuiRepaintTableView();
extern void GuiUpdatePatches();
extern void GuiUpdateCallStack();
extern void GuiUpdateMemoryView();

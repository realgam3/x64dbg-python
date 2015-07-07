%module _scriptapi
%{
#include <windows.h>
#include "_scriptapi.h"
#include "_scriptapi_debug.h"
#include "_scriptapi_memory.h"
#include "_scriptapi_register.h"
#include "_scriptapi_pattern.h"
#include "_scriptapi_gui.h"
#include "_scriptapi_misc.h"
#include "_scriptapi_stack.h"
#include "_scriptapi_assembler.h"
%}

%include <windows.i>
#ifndef PLUG_IMPEXP
#ifdef BUILD_DBG
#define PLUG_IMPEXP __declspec(dllexport)
#else
#define PLUG_IMPEXP __declspec(dllimport)
#endif //BUILD_DBG
#endif //PLUG_IMPEXP

#define SCRIPT_EXPORT PLUG_IMPEXP

%include "..\pluginsdk\_scriptapi_debug.h"

// Type Maps
%include <pybuffer.i>
%pybuffer_string(void* data);
%apply duint *OUTPUT { duint *sizeRead };
%apply duint *OUTPUT { duint *sizeWritten };
%pybuffer_binary(parm, size_parm)

%rename(Memory_Read) Script::Memory::Read;
%rename(Memory_Write) Script::Memory::Write;

%include "..\pluginsdk\_scriptapi_memory.h"

%include "..\pluginsdk\_scriptapi_register.h"
%include "..\pluginsdk\_scriptapi_pattern.h"

%rename(Gui_SelectionGet) Script::Gui::SelectionGet;
%rename(Gui_SelectionSet) Script::Gui::SelectionSet;
%rename(Gui_SelectionGetStart) Script::Gui::SelectionGetStart;
%rename(Gui_SelectionGetEnd) Script::Gui::SelectionGetEnd;

%rename(Disassembly_SelectionGet) Script::Gui::Disassembly::SelectionGet;
%rename(Disassembly_SelectionSet) Script::Gui::Disassembly::SelectionSet;
%rename(Disassembly_SelectionGetStart) Script::Gui::Disassembly::SelectionGetStart;
%rename(Disassembly_SelectionGetEnd) Script::Gui::Disassembly::SelectionGetEnd;

%rename(Dump_SelectionGet) Script::Gui::Dump::SelectionGet;
%rename(Dump_SelectionSet) Script::Gui::Dump::SelectionSet;
%rename(Dump_SelectionGetStart) Script::Gui::Dump::SelectionGetStart;
%rename(Dump_SelectionGetEnd) Script::Gui::Dump::SelectionGetEnd;

%rename(Stack_SelectionGet) Script::Gui::Stack::SelectionGet;
%rename(Stack_SelectionSet) Script::Gui::Stack::SelectionSet;
%rename(Stack_SelectionGetStart) Script::Gui::Stack::SelectionGetStart;
%rename(Stack_SelectionGetEnd) Script::Gui::Stack::SelectionGetEnd;

%apply duint *OUTPUT { duint *start };
%apply duint *OUTPUT { duint *end };

%include "..\pluginsdk\_scriptapi_gui.h"

%include "..\pluginsdk\_scriptapi_misc.h"
%include "..\pluginsdk\_scriptapi_stack.h"
%include "..\pluginsdk\_scriptapi_assembler.h"

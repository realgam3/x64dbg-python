from .. import _x64dbg

# Script::Gui
def Gui_SelectionGet(window):
    result, start, end = _x64dbg.Gui_SelectionGet(window)
    if result:
        return start, end

def Gui_SelectionSet(window, start, end):
    return _x64dbg.Gui_SelectionSet(window, start, end)

def Gui_SelectionGetStart(window):
    return _x64dbg.Gui_SelectionGetStart(window)

def Gui_SelectionGetEnd(window):
    return _x64dbg.Gui_SelectionGetEnd(window)


# Script::Gui::Disassembly
def Disassembly_SelectionGet():
    result, start, end = _x64dbg.Disassembly_SelectionGet()
    if result:
        return start, end

def Disassembly_SelectionSet(start, end):
    return _x64dbg.Disassembly_SelectionSet(start, end)

def Disassembly_SelectionGetStart():
    return _x64dbg.Disassembly_SelectionGetStart()

def Disassembly_SelectionGetEnd():
    return _x64dbg.Disassembly_SelectionGetEnd()


# Script::Gui::Dump
def Dump_SelectionGet():
    result, start, end = _x64dbg.Dump_SelectionGet()
    if result:
        return start, end

def Dump_SelectionSet(start, end):
    return _x64dbg.Dump_SelectionSet(start, end)

def Dump_SelectionGetStart():
    return _x64dbg.Dump_SelectionGetStart()

def Dump_SelectionGetEnd():
    return _x64dbg.Dump_SelectionGetEnd()


# Script::Gui::Stack
def Stack_SelectionGet():
    result, start, end = _x64dbg.Stack_SelectionGet()
    if result:
        return start, end

def Stack_SelectionSet(start, end):
    return _x64dbg.Stack_SelectionSet(start, end)

def Stack_SelectionGetStart():
    return _x64dbg.Stack_SelectionGetStart()

def Stack_SelectionGetEnd():
    return _x64dbg.Stack_SelectionGetEnd()

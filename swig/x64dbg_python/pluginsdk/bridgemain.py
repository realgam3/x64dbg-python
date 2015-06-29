import ctypes
import _x64dbg
# from ..utils import is_64bit


GUI_MAX_LINE_SIZE = 65536

# duint = ctypes.c_ulonglong if is_64bit() else ctypes.c_ulong
# dsint = ctypes.c_longlong if is_64bit() else ctypes.c_long


def DbgIsDebugging():
    return _x64dbg.DbgIsDebugging()

def GuiGetLineWindow(title=''):
    line = ctypes.create_string_buffer(GUI_MAX_LINE_SIZE)
    return_value = _x64dbg.GuiGetLineWindow("%s" % title, line)
    if return_value:
        return line.value

def GuiGetWindowHandle():
    return _x64dbg.GuiGetWindowHandle()

import ctypes
from .. import _x64dbg


MAX_ERROR_SIZE = 512


def Assemble(addr, instruction):
    byte_array = bytearray()
    result, size = _x64dbg.Assemble(addr, byte_array, instruction)
    if result:
        return byte_array[:size]

def AssembleEx(addr, instruction):
    error = ctypes.create_string_buffer(MAX_ERROR_SIZE)
    byte_array = bytearray()
    result, size = _x64dbg.AssembleEx(addr, byte_array, instruction, error)
    if not result:
        raise Exception(error)
    return byte_array[:size]

def AssembleMem(addr, instruction):
    return _x64dbg.AssembleMem(addr, instruction)

def AssembleMemEx(addr, instruction, fillnop):
    error = ctypes.create_string_buffer(MAX_ERROR_SIZE)
    result, size = _x64dbg.AssembleMemEx(addr, instruction, error, fillnop)
    if not result:
        raise Exception(error)
    return result[:size]

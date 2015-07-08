import ctypes
from .. import _x64dbg


MAX_ERROR_SIZE = 512
MAX_STRING = 512


def Assemble(instruction, addr=0):
    dest = ctypes.create_string_buffer(MAX_STRING)
    result, size = _x64dbg.Assemble(addr, dest, instruction)
    if result:
        return dest[:size].encode('hex')

def AssembleEx(instruction, addr=0):
    error = ctypes.create_string_buffer(MAX_ERROR_SIZE)
    dest = ctypes.create_string_buffer(MAX_STRING)
    result, size = _x64dbg.AssembleEx(addr, dest, instruction, error)
    if not result:
        raise Exception(error.value)
    return dest[:size].encode('hex')

def AssembleMem(instruction, addr):
    return _x64dbg.AssembleMem(addr, instruction)

def AssembleMemEx(instruction, fillnop, addr):
    error = ctypes.create_string_buffer(MAX_ERROR_SIZE)
    result, size = _x64dbg.AssembleMemEx(addr, instruction, error, fillnop)
    if not result:
        raise Exception(error.value)
    return result

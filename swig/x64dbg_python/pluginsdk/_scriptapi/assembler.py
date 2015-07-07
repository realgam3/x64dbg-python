import ctypes
from .. import _x64dbg

MAX_ERROR_SIZE = 60

SCRIPT_EXPORT bool Assemble(duint addr, unsigned char* dest, int* size, const char* instruction); //dest[16]
SCRIPT_EXPORT bool AssembleEx(duint addr, unsigned char* dest, int* size, const char* instruction, char* error); //dest[16], error[MAX_ERROR_SIZE]
SCRIPT_EXPORT bool AssembleMem(duint addr, const char* instruction);
SCRIPT_EXPORT bool AssembleMemEx(duint addr, const char* instruction, int* size, char* error, bool fillnop); //error[MAX_ERROR_SIZE]
def Assemble(addr, instruction):
    size =
    return _x64dbg.Assemble(addr, instruction)

def AssembleEx(addr, instruction):
    return _x64dbg.AssembleEx(addr, instruction)

def AssembleMem(addr, instruction):
    return _x64dbg.AssembleMem(addr, instruction)

def AssembleMemEx(addr, instruction, fillnop):
    return _x64dbg.AssembleMemEx(addr, instruction, fillnop)

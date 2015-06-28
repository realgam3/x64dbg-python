from .. import _x64dbg


def ReadByte(addr):
    return _x64dbg.ReadByte(addr)

def WriteByte(addr, data):
    return _x64dbg.WriteByte(addr, data)

def ReadDword(addr):
    return _x64dbg.ReadDword(addr)

def WriteDword(addr, data):
    return _x64dbg.WriteDword(addr, data)

# TODO: Add All Memory Functions

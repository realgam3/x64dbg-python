from x64dbg_python.utils import is_64bit
from .. import _x64dbg


def Read(addr, size):
    read_bytes = bytearray(size)
    result, read_size = _x64dbg.Read(addr, read_bytes, size)
    return bytes(read_bytes[:read_size])

def Write(addr, data):
    result, write_size = _x64dbg.Write(addr, data, len(data))
    return result

def ReadByte(addr):
    return _x64dbg.ReadByte(addr)

def WriteByte(addr, data):
    return _x64dbg.WriteByte(addr, data)

def ReadWord(addr):
    return _x64dbg.ReadWord(addr)

def WriteWord(addr, data):
    return _x64dbg.WriteWord(addr, data)

def ReadDword(addr):
    return _x64dbg.ReadDword(addr)

def WriteDword(addr, data):
    return _x64dbg.WriteDword(addr, data)

if is_64bit():
    def ReadQword(addr):
        return _x64dbg.ReadQword(addr)

    def WriteQword(addr, data):
        return _x64dbg.WriteQword(addr, data)

def ReadPtr(addr):
    return _x64dbg.ReadPtr(addr)

def WritePtr(addr, data):
    return _x64dbg.WritePtr(addr, data)

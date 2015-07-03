from .. import _x64dbg


def Find(data, pattern):
    return _x64dbg.Find(data, len(data), pattern)

def FindMem(start, size, pattern):
    return _x64dbg.FindMem(start, size, pattern)

def Write(data, pattern):
    _x64dbg.Write(data, len(data), pattern)

def WriteMem(start, size, pattern):
    _x64dbg.WriteMem(start, size, pattern)

def SearchAndReplace(data, searchpattern, replacepattern):
    return _x64dbg.SearchAndReplace(data, len(data), searchpattern, replacepattern)

def SearchAndReplaceMem(start, size, searchpattern, replacepattern):
    return _x64dbg.SearchAndReplaceMem(start, size, searchpattern, replacepattern)

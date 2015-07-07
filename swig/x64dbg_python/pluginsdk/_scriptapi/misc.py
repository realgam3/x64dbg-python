from .. import _x64dbg


def ParseExpression(expression, value):
    return _x64dbg.ParseExpression(expression, value)

def RemoteGetProcAddress(module, api):
    return _x64dbg.RemoteGetProcAddress(module, api)

def ResolveLabel(label):
    return _x64dbg.ResolveLabel(label)

def Alloc(size):
    return _x64dbg.Alloc(size)

def Free(ptr):
    return _x64dbg.Free(ptr)

from .. import _x64dbg


def Pop():
    return _x64dbg.Pop()

def Push(value):
    # returns the previous top, equal to Peek(1)
    return _x64dbg.Push(value)

def Peek(offset=0):
    # offset is in multiples of Register::Size(), for easy x32/x64 portability
    return _x64dbg.Peek(offset)

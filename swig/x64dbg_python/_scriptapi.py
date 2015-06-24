import _x64dbg


# Debug
def Wait():
    _x64dbg.Wait()

def Run():
    _x64dbg.Run()

def Stop():
    _x64dbg.Stop()

def StepIn():
    _x64dbg.StepIn()

def StepOver():
    _x64dbg.StepOver()

def StepOut():
    _x64dbg.StepOut()


# Memory
def ReadByte(addr):
    return _x64dbg.ReadByte(addr)

def WriteByte(addr, data):
    return _x64dbg.WriteByte(addr, data)

def ReadDword(addr):
    return _x64dbg.ReadDword(addr)

def WriteDword(addr, data):
    return _x64dbg.WriteDword(addr, data)


# Register
def GetEAX():
    return _x64dbg.GetEAX()

def SetEAX(value):
    return _x64dbg.SetEAX(value)

def GetEBX():
    return _x64dbg.GetEBX()

def SetEBX(value):
    return _x64dbg.SetEBX(value)

def GetECX():
    return _x64dbg.GetECX()

def SetECX(value):
    return _x64dbg.SetECX(value)

def GetEDX():
    return _x64dbg.GetEDX()

def SetEDX(value):
    return _x64dbg.SetEDX(value)

def GetEBP():
    return _x64dbg.GetEBP()

def SetEBP(value):
    return _x64dbg.SetEBP(value)

def GetESP():
    return _x64dbg.GetESP()

def SetESP(value):
    return _x64dbg.SetESP(value)

def GetEDI():
    return _x64dbg.GetEDI()

def SetEDI(value):
    return _x64dbg.SetEDI(value)

def GetESI():
    return _x64dbg.GetESI()

def SetESI(value):
    return _x64dbg.SetESI(value)

def GetEIP():
    return _x64dbg.GetEIP()

def SetEIP(value):
    return _x64dbg.SetEIP(value)

# TODO: Add All Memory Functions, Add x64 Register Functions

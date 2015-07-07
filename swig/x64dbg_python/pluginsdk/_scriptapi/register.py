from x64dbg_python.utils import is_64bit
from .. import _x64dbg


# x86 Registers
def GetEAX():
    return _x64dbg.GetEAX()

def SetEAX(value):
    return _x64dbg.SetEAX(value)

def GetAX():
    return _x64dbg.GetAX()

def SetAX(value):
    return _x64dbg.SetAX(value)

def GetAH():
    return _x64dbg.GetAH()

def SetAH(value):
    return _x64dbg.SetAH(value)

def GetAL():
    return _x64dbg.GetAL()

def SetAL(value):
    return _x64dbg.SetAL(value)

def GetEBX():
    return _x64dbg.GetEBX()

def SetEBX(value):
    return _x64dbg.SetEBX(value)

def GetBX():
    return _x64dbg.GetBX()

def SetBX(value):
    return _x64dbg.SetBX(value)

def GetBH():
    return _x64dbg.GetBH()

def SetBH(value):
    return _x64dbg.SetBH(value)

def GetBL():
    return _x64dbg.GetBL()

def SetBL(value):
    return _x64dbg.SetBL(value)

def GetECX():
    return _x64dbg.GetECX()

def SetECX(value):
    return _x64dbg.SetECX(value)

def GetCX():
    return _x64dbg.GetCX()

def SetCX(value):
    return _x64dbg.SetCX(value)

def GetCH():
    return _x64dbg.GetCH()

def SetCH(value):
    return _x64dbg.SetCH(value)

def GetCL():
    return _x64dbg.GetCL()

def SetCL(value):
    return _x64dbg.SetCL(value)

def GetEDX():
    return _x64dbg.GetEDX()

def SetEDX(value):
    return _x64dbg.SetEDX(value)

def GetDX():
    return _x64dbg.GetDX()

def SetDX(value):
    return _x64dbg.SetDX(value)

def GetDH():
    return _x64dbg.GetDH()

def SetDH(value):
    return _x64dbg.SetDH(value)

def GetDL():
    return _x64dbg.GetDL()

def SetDL(value):
    return _x64dbg.SetDL(value)

def GetEDI():
    return _x64dbg.GetEDI()

def SetEDI(value):
    return _x64dbg.SetEDI(value)

def GetDI():
    return _x64dbg.GetDI()

def SetDI(value):
    return _x64dbg.SetDI(value)

def GetESI():
    return _x64dbg.GetESI()

def SetESI(value):
    return _x64dbg.SetESI(value)

def GetSI():
    return _x64dbg.GetSI()

def SetSI(value):
    return _x64dbg.SetSI(value)

def GetEBP():
    return _x64dbg.GetEBP()

def SetEBP(value):
    return _x64dbg.SetEBP(value)

def GetBP():
    return _x64dbg.GetBP()

def SetBP(value):
    return _x64dbg.SetBP(value)

def GetESP():
    return _x64dbg.GetESP()

def SetESP(value):
    return _x64dbg.SetESP(value)

def GetSP():
    return _x64dbg.GetSP()

def SetSP(value):
    return _x64dbg.SetSP(value)

def GetEIP():
    return _x64dbg.GetEIP()

def SetEIP(value):
    return _x64dbg.SetEIP(value)


# x86 Debug Registers
def GetDR0():
    return _x64dbg.GetDR0()

def SetDR0(value):
    return _x64dbg.SetDR0(value)

def GetDR1():
    return _x64dbg.GetDR1()

def SetDR1(value):
    return _x64dbg.SetDR1(value)

def GetDR2():
    return _x64dbg.GetDR2()

def SetDR2(value):
    return _x64dbg.SetDR2(value)

def GetDR3():
    return _x64dbg.GetDR3()

def SetDR3(value):
    return _x64dbg.SetDR3(value)

def GetDR6():
    return _x64dbg.GetDR6()

def SetDR6(value):
    return _x64dbg.SetDR6(value)

def GetDR7():
    return _x64dbg.GetDR7()

def SetDR7(value):
    return _x64dbg.SetDR7(value)


# x64 Registers
if is_64bit():
    def GetRAX():
        return _x64dbg.GetRAX()

    def SetRAX(value):
        return _x64dbg.SetRAX(value)

    def GetRBX():
        return _x64dbg.GetRBX()

    def SetRBX(value):
        return _x64dbg.SetRBX(value)

    def GetRCX():
        return _x64dbg.GetRCX()

    def SetRCX(value):
        return _x64dbg.SetRCX(value)

    def GetRDX():
        return _x64dbg.GetRDX()

    def SetRDX(value):
        return _x64dbg.SetRDX(value)

    def GetRSI():
        return _x64dbg.GetRSI()

    def SetRSI(value):
        return _x64dbg.SetRSI(value)

    def GetSIL():
        return _x64dbg.GetSIL()

    def SetSIL(value):
        return _x64dbg.SetSIL(value)

    def GetRDI():
        return _x64dbg.GetRDI()

    def SetRDI(value):
        return _x64dbg.SetRDI(value)

    def GetDIL():
        return _x64dbg.GetDIL()

    def SetDIL(value):
        return _x64dbg.SetDIL(value)

    def GetRBP():
        return _x64dbg.GetRBP()

    def SetRBP(value):
        return _x64dbg.SetRBP(value)

    def GetBPL():
        return _x64dbg.GetBPL()

    def SetBPL(value):
        return _x64dbg.SetBPL(value)

    def GetRSP():
        return _x64dbg.GetRSP()

    def SetRSP(value):
        return _x64dbg.SetRSP(value)

    def GetSPL():
        return _x64dbg.GetSPL()

    def SetSPL(value):
        return _x64dbg.SetSPL(value)

    def GetRIP():
        return _x64dbg.GetRIP()

    def SetRIP(value):
        return _x64dbg.SetRIP(value)

    def GetR8():
        return _x64dbg.GetR8()

    def SetR8(value):
        return _x64dbg.SetR8(value)

    def GetR8D():
        return _x64dbg.GetR8D()

    def SetR8D(value):
        return _x64dbg.SetR8D(value)

    def GetR8W():
        return _x64dbg.GetR8W()

    def SetR8W(value):
        return _x64dbg.SetR8W(value)

    def GetR8B():
        return _x64dbg.GetR8B()

    def SetR8B(value):
        return _x64dbg.SetR8B(value)

    def GetR9():
        return _x64dbg.GetR9()

    def SetR9(value):
        return _x64dbg.SetR9(value)

    def GetR9D():
        return _x64dbg.GetR9D()

    def SetR9D(value):
        return _x64dbg.SetR9D(value)

    def GetR9W():
        return _x64dbg.GetR9W()

    def SetR9W(value):
        return _x64dbg.SetR9W(value)

    def GetR9B():
        return _x64dbg.GetR9B()

    def SetR9B(value):
        return _x64dbg.SetR9B(value)

    def GetR10():
        return _x64dbg.GetR10()

    def SetR10(value):
        return _x64dbg.SetR10(value)

    def GetR10D():
        return _x64dbg.GetR10D()

    def SetR10D(value):
        return _x64dbg.SetR10D(value)

    def GetR10W():
        return _x64dbg.GetR10W()

    def SetR10W(value):
        return _x64dbg.SetR10W(value)

    def GetR10B():
        return _x64dbg.GetR10B()

    def SetR10B(value):
        return _x64dbg.SetR10B(value)

    def GetR11():
        return _x64dbg.GetR11()

    def SetR11(value):
        return _x64dbg.SetR11(value)

    def GetR11D():
        return _x64dbg.GetR11D()

    def SetR11D(value):
        return _x64dbg.SetR11D(value)

    def GetR11W():
        return _x64dbg.GetR11W()

    def SetR11W(value):
        return _x64dbg.SetR11W(value)

    def GetR11B():
        return _x64dbg.GetR11B()

    def SetR11B(value):
        return _x64dbg.SetR11B(value)

    def GetR12():
        return _x64dbg.GetR12()

    def SetR12(value):
        return _x64dbg.SetR12(value)

    def GetR12D():
        return _x64dbg.GetR12D()

    def SetR12D(value):
        return _x64dbg.SetR12D(value)

    def GetR12W():
        return _x64dbg.GetR12W()

    def SetR12W(value):
        return _x64dbg.SetR12W(value)

    def GetR12B():
        return _x64dbg.GetR12B()

    def SetR12B(value):
        return _x64dbg.SetR12B(value)

    def GetR13():
        return _x64dbg.GetR13()

    def SetR13(value):
        return _x64dbg.SetR13(value)

    def GetR13D():
        return _x64dbg.GetR13D()

    def SetR13D(value):
        return _x64dbg.SetR13D(value)

    def GetR13W():
        return _x64dbg.GetR13W()

    def SetR13W(value):
        return _x64dbg.SetR13W(value)

    def GetR13B():
        return _x64dbg.GetR13B()

    def SetR13B(value):
        return _x64dbg.SetR13B(value)

    def GetR14():
        return _x64dbg.GetR14()

    def SetR14(value):
        return _x64dbg.SetR14(value)

    def GetR14D():
        return _x64dbg.GetR14D()

    def SetR14D(value):
        return _x64dbg.SetR14D(value)

    def GetR14W():
        return _x64dbg.GetR14W()

    def SetR14W(value):
        return _x64dbg.SetR14W(value)

    def GetR14B():
        return _x64dbg.GetR14B()

    def SetR14B(value):
        return _x64dbg.SetR14B(value)

    def GetR15():
        return _x64dbg.GetR15()

    def SetR15(value):
        return _x64dbg.SetR15(value)

    def GetR15D():
        return _x64dbg.GetR15D()

    def SetR15D(value):
        return _x64dbg.SetR15D(value)

    def GetR15W():
        return _x64dbg.GetR15W()

    def SetR15W(value):
        return _x64dbg.SetR15W(value)

    def GetR15B():
        return _x64dbg.GetR15B()

    def SetR15B(value):
        return _x64dbg.SetR15B(value)


# Generic Registers
def GetCIP():
    return _x64dbg.GetCIP()

def SetCIP(value):
    return _x64dbg.SetCIP(value)

def GetCSP():
    return _x64dbg.GetCSP()

def SetCSP(value):
    return _x64dbg.SetCSP(value)

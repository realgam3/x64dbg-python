import sys
from pluginsdk import _scriptapi


X86_DEBUG_REGISTERS = (
    'DR0', 'DR1', 'DR2', 'DR3', 'DR6', 'DR7'
)
X86_REGISTERS = (
    'EAX', 'AX', 'AH', 'AL',
    'EBX', 'BX', 'BH', 'BL',
    'ECX', 'CX', 'CH', 'CL',
    'EDX', 'DX', 'DH', 'DL',
    'EDI', 'DI', 'ESI', 'SI',
    'EBP', 'BP', 'ESP', 'SP',
    'EIP'
    'CIP',  # Generic EIP/RIP register
) + X86_DEBUG_REGISTERS


def is_64bit():
    return sys.maxsize > 2**32


class Register(object):
    def __get_reg_function(self, register, get=True):
        register_name = register.upper()
        if not is_64bit() and register_name not in X86_REGISTERS:
            raise Exception("Not an x86 register.")

        return getattr(
            _scriptapi,
            '{method}{register}'.format(
                method='Get' if get else 'Set',
                register=register_name
            ),
        )

    def __getattr__(self, item):
        return self.__get_reg_function(item)()

    def __setattr__(self, key, value):
        self.__get_reg_function(key, get=False)(value)

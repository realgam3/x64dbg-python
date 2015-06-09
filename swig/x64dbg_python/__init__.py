__author__ = 'Tomer Zait (RealGame)'
__version__ = '1.0.0'

import sys
from bridgemain import *
from _plugins import _plugin_logprintf, _plugin_logputs


def raw_input(prompt=''):
    return GuiGetLineWindow(prompt)


def input(prompt=''):
    return eval(GuiGetLineWindow(prompt))


class OutputHook(object):
    def __init__(self, stream_name='stdout', callback=_plugin_logprintf):
        self.is_hooking = False
        self.callback = callback

        self.stream_name = stream_name
        if self.stream_name not in ['stderr', 'stdout']:
            raise Exception('Cannot hook %s stream.' % self.stream_name)
        elif self.__is_hooked():
            raise Exception('Do not hook the hooker!')

        self.__original_stream = getattr(sys, self.stream_name)

    def __getattr__(self, name):
        return getattr(self.__original_stream, name)

    def __is_hooked(self):
        stream = getattr(sys, self.stream_name)
        return hasattr(stream, 'is_hooking')

    def write(self, text):
        self.callback(text)

    def start(self):
        if not self.is_hooking:
            setattr(sys, self.stream_name, self)
            self.is_hooking = True

    def stop(self):
        if self.is_hooking:
            setattr(sys, self.stream_name, self.__original_stream)
            self.is_hooking = False

# Hook sys.stdout
STDOUT_HOOK = OutputHook('stdout')
STDOUT_HOOK.start()

# Hook sys.stderr
STDERR_HOOK = OutputHook('stderr')
STDERR_HOOK.start()

# Print Message That The Hooks Worked!
print '[PYTHON] stdout, stderr, raw_input hooked!'

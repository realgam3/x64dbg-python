import sys
import ctypes
import _x64dbg

GUI_MAX_LINE_SIZE = 65536
STDERR_BUFFER = ''


def _plugin_logputs(text=''):
    _x64dbg._plugin_logputs('%s' % text)


def GuiGetLineWindow(title=''):
    line = ctypes.create_string_buffer(GUI_MAX_LINE_SIZE)
    return_value = _x64dbg.GuiGetLineWindow("%s" % title, line)
    if return_value:
        return line.value


# StdStreamHooker - Taken From ollydbg2-plugin (https://github.com/0vercl0k/ollydbg2-python)
class StdStreamHooker:
    """
    This class is able to hook the python stdout or the stderr stream.
    You can use it to forward all the content displayed on stdout/stderr where you want!
    """

    def __init__(self, which_stream='stdout'):
        """
        You can hook only the stdout or the stderr python stream
        """
        assert (which_stream in ['stdout', 'stderr'])
        self.hook_func = None
        self.real_stream = None
        self.which_stream = which_stream

    def start(self, func):
        """
        Let the show begins -- this method starts the hooking GetProcAddress
        """
        self.hook_func = func
        if self.which_stream == 'stdout':
            self.real_stream = sys.stdout
            sys.stdout = self
        else:
            sys.real_stream = sys.stderr
            sys.stderr = self

    def stop(self):
        """
        Unhook the stream you've hooked
        """
        if self.real_stream != None:
            self.real_stream.flush()
            self.real_stream = None

            if self.which_stream == 'stdout':
                sys.stdout = sys.__stdout__
            else:
                sys.stderr = sys.__stderr__

            self.hook_func = None

    def write(self, s):
        """
        This is a proxy-function that will forward the write processing to your hook method.

        In fact, when a piece of code will call sys.stdout.write, StdStreamHooker will be called and
        it will simply forward the call to your own method ; in order to whatever you need to.

        Little schema:
        sys.stdout.write -> StdStreamHooker.write -> your own method
        """
        return self.hook_func(s)

    def __getattr__(self, n):
        """
        This methods is a forwarder method ; when pieces of code will call methods don't
        overloaded by StdStreamHooker, you have to forward them to the original stream class.

        For example, if someone to stuff like sys.stdout.fflush(), the StdStreamHooker doesn't
        have any implementation for that method, and we don't want to reimplement the methods
        available in std.stdout/stderr. So here is a simple code that explains the __getattr__ trick:

        >>> class A():
        ...     def __init__(self):
        ...             print 'hi, this is the constructor'
        ...     def methoda(self):
        ...             print 'this is methoda'
        ...     def __getattr__(self, n):
        ...             print 'getattr:n'
        ...
        >>> a = A()
        hi, this is the constructor
        >>> a.methoda()
        this is methoda
        >>> a.methodb()
        getattr:n
        [..]
        >>> a.method_undefined()
        getattr:n
        [..]
        """
        return self.real_stream.__getattr__(n)


def hook_method(s):
    """
    This is the hook method for the stdout stream, it tries to
    respect the '\n' in your strings in order to have a clean
    output in the ollydbg log window
    """
    # yeah, each time you do a print 'something' python call two times
    # sys.stdout.write ; first with the string 'something' and the second
    # with only an '\n'
    if len(s) == 1 and s[0] == '\n':
        return

    # now ollydbg just don't care if you have an '\n' in your string
    # it will just display the string added to the list on a single line
    # whatever the string is.
    # The trick is to do other calls to addtolist to emulate a '\n'
    chunks = s.split('\n')
    for substr in chunks:
        _plugin_logputs(substr)


def hook_method_stderr(s):
    """
    Trying to bufferize the stream in order to have a proper
    output in the ollydbg log window.

    Each time you call Addtolist it displays a new line, so we keep
    a global buffer until we find an '\n' ; if we found one we display
    the whole buffer, if not we just concatenate the string to the global
    buffer.
    """
    global STDERR_BUFFER
    idx = s.find('\n')
    if idx != -1:
        if len(s) == 1:
            _plugin_logputs(STDERR_BUFFER)
            STDERR_BUFFER = ''
        else:
            STDERR_BUFFER += s[:idx]
            _plugin_logputs(STDERR_BUFFER)
            if idx != len(s):
                STDERR_BUFFER = s[idx + 1:]
            else:
                STDERR_BUFFER = ''
    else:
        # We keep in memory the buffer until finding an '\n'
        # in order to have a clean output in the log window
        STDERR_BUFFER += s


p_stdout = StdStreamHooker('stdout')
p_stderr = StdStreamHooker('stderr')

p_stdout.start(hook_method)
p_stderr.start(hook_method_stderr)

_plugin_logpprintf = _plugin_logputs
raw_input = GuiGetLineWindow

print '[PYTHON] stdout, stderr, raw_input hooked!'

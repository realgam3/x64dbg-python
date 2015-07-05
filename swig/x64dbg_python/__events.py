import types

class Event(object):
    def __init__(self):
        self.init_debug = None

    def listen(self, event_name, callback):
        if not hasattr(self, event_name.lower()):
            raise Exception("%s Is not a valid event." % event_name)
        if not isinstance(callback, types.FunctionType):
            raise Exception("Invalid callback function.")

        self.init_debug = callback

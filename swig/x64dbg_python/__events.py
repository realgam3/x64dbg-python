import functools
import types

EVENTS = [
    'breakpoint',
]

class Event(object):
    def __init__(self):
        self.breakpoint = None

    def listen(self, event_name, callback):
        event_name_lower = event_name.lower()
        if event_name_lower not in EVENTS:
            raise Exception("%s Is not a valid event." % event_name_lower)
        if not isinstance(callback, types.FunctionType):
            raise Exception("Invalid callback function.")

        _function = getattr(self, "_" + event_name_lower)
        setattr(self, event_name_lower, functools.partial(_function, callback=callback))

    def _breakpoint(self, type, addr, enabled, singleshoot, active, name, mod, slot, callback=None):
        """
        typedef struct
        {
            BPXTYPE type;
            duint addr;
            bool enabled;
            bool singleshoot;
            bool active;
            char name[MAX_BREAKPOINT_SIZE];
            char mod[MAX_MODULE_SIZE];
            unsigned short slot;
        } BRIDGEBP;

        typedef enum
        {
            bp_none = 0,
            bp_normal = 1,
            bp_hardware = 2,
            bp_memory = 4
        } BPXTYPE;
        """
        callback(type, addr, enabled, singleshoot, active, name, mod, slot)

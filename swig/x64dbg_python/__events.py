
EVENTS = [
    'breakpoint',
    'stop_debug',
    'create_process',
]

class Event(object):
    def __init__(self):
        # Keys: type, addr, enabled, singleshoot, active, name, mod, slot
        # typedef struct
        # {
        #     BPXTYPE type;
        #     duint addr;
        #     bool enabled;
        #     bool singleshoot;
        #     bool active;
        #     char name[MAX_BREAKPOINT_SIZE];
        #     char mod[MAX_MODULE_SIZE];
        #     unsigned short slot;
        # } BRIDGEBP;
        #
        # typedef enum
        # {
        #     bp_none = 0,
        #     bp_normal = 1,
        #     bp_hardware = 2,
        #     bp_memory = 4
        # } BPXTYPE;
        self.breakpoint = None
        # Keys: None
        self.stop_debug = None
        # Keys: CreateProcessInfo, modInfo, DebugFileName, fdProcessInfo
        # typedef struct
        # {
        #     CREATE_PROCESS_DEBUG_INFO* CreateProcessInfo;
        #     IMAGEHLP_MODULE64* modInfo;
        #     const char* DebugFileName;
        #     PROCESS_INFORMATION* fdProcessInfo;
        # } PLUG_CB_CREATEPROCESS;
        self.create_process = None

    def listen(self, event_name, callback):
        """
        Listen to event with a callback,
        Callback should always get key word arguments(kwargs).

        For example:
        def callback(**kwargs):
            print kwargs
        """
        event_name_lower = event_name.lower()
        if event_name_lower not in EVENTS:
            raise Exception("%s Is not a valid event." % event_name_lower)

        setattr(self, event_name_lower, callback)

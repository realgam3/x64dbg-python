%module _plugins
%{
#include <windows.h>
#include "_plugins.h"
%}

%include <windows.i>
#ifndef PLUG_IMPEXP
#ifdef BUILD_DBG
#define PLUG_IMPEXP __declspec(dllexport)
#else
#define PLUG_IMPEXP __declspec(dllimport)
#endif //BUILD_DBG
#endif //PLUG_IMPEXP

PLUG_IMPEXP void _plugin_registercallback(int pluginHandle, CBTYPE cbType, CBPLUGIN cbPlugin);
PLUG_IMPEXP bool _plugin_unregistercallback(int pluginHandle, CBTYPE cbType);
PLUG_IMPEXP bool _plugin_registercommand(int pluginHandle, const char* command, CBPLUGINCOMMAND cbCommand, bool debugonly);
PLUG_IMPEXP bool _plugin_unregistercommand(int pluginHandle, const char* command);
PLUG_IMPEXP void _plugin_logprintf(const char* format, ...);
PLUG_IMPEXP void _plugin_logputs(const char* text);
PLUG_IMPEXP void _plugin_debugpause();
PLUG_IMPEXP void _plugin_debugskipexceptions(bool skip);
PLUG_IMPEXP int _plugin_menuadd(int hMenu, const char* title);
PLUG_IMPEXP bool _plugin_menuaddentry(int hMenu, int hEntry, const char* title);
PLUG_IMPEXP bool _plugin_menuaddseparator(int hMenu);
PLUG_IMPEXP bool _plugin_menuclear(int hMenu);
PLUG_IMPEXP void _plugin_menuseticon(int hMenu, const ICONDATA* icon);
PLUG_IMPEXP void _plugin_menuentryseticon(int pluginHandle, int hEntry, const ICONDATA* icon);
PLUG_IMPEXP void _plugin_startscript(CBPLUGINSCRIPT cbScript);
PLUG_IMPEXP bool _plugin_waituntilpaused();

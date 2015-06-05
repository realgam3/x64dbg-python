%module _x64dbg
%{
#include "bridgemain.h"
#include "_plugins.h"
%}
// bridgemain.h
%include<pybuffer.i> 
%pybuffer_string(char* text); 
extern bool GuiGetLineWindow(const char* title, char* text);
 
// _plugins.h
extern void _plugin_logputs(const char* text);
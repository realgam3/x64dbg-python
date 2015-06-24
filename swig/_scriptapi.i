%module _scriptapi
%{
#include "_scriptapi.h"
%}

#ifdef _WIN64
typedef unsigned long long duint;
typedef signed long long dsint;
#else
typedef unsigned long duint;
typedef signed long dsint;
#endif //_WIN64

%include "_plugins.i"
%include "../pluginsdk/_scriptapi.h"

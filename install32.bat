@echo off
set PLUGINDIR=..\x64_dbg\bin\x32\plugins
mkdir %PLUGINDIR%
copy bin\x32\x64dbg-python.dll %PLUGINDIR%\x64dbg_python.dp32
mkdir %PLUGINDIR%\x64dbg_python
copy swig\build\lib.win32-2.7\* %PLUGINDIR%\x64dbg_python
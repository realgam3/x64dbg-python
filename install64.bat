@echo off
set PLUGINDIR=..\x64_dbg\bin\x64\plugins
mkdir %PLUGINDIR%
copy bin\x64\x64dbg-python.dll %PLUGINDIR%\x64dbg_python.dp64
xcopy /e /c /y swig\build\lib.win-amd64-2.7\x64dbg_python %PLUGINDIR%\x64dbg_python\
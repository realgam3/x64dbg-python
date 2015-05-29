@echo off
set PLUGINDIR=..\x64_dbg\bin\x32\plugins
mkdir %PLUGINDIR%
copy bin\x32\testplugin.dll %PLUGINDIR%\testplugin.dp32
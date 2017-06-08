@echo off
call "E:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools\VsDevCmd.bat"
cd "%~dp0"
RC.exe /nologo /r TinyURL.rc
cl.exe /nologo /Tc "TinyURL.c" /I E:\Python360\include E:\Python360\libs\python36.lib /link /NOLOGO /OUT:"TinyURL.exe" /SUBSYSTEM:CONSOLE "TinyURL.res" /FIXED
call "E:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" amd64
cd "%~dp0"
RC.exe /nologo /r TinyURL.rc
cl.exe /nologo /Tc "TinyURL.c" /I E:\Python361x64\include E:\Python361x64\libs\python36.lib /link /NOLOGO /OUT:"x64_build\TinyURL.exe" /SUBSYSTEM:CONSOLE "TinyURL.res" /FIXED
pause
@echo off
setlocal
set "currentDir=%~dp0"
cd /d "%currentDir%..\assets\documentacion-tecnica\docs\build\html"
start "" "index.html"
endlocal

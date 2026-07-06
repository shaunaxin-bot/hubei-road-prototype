@echo off
chcp 65001 >nul
echo =======================================================
echo  Hubei Road Data Platform
echo  Standalone Edition
echo =======================================================
echo.
echo  [1/2] Starting local offline server...
echo  [2/2] Opening browser...
echo.
echo  Please DO NOT close this black window! Closing it stops the server!
echo =======================================================
timeout /t 1 /nobreak >nul
start msedge "http://localhost:8000/index.html?mode=standalone&view=deepqa"
server.exe
pause

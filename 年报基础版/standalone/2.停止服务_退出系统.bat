@echo off
chcp 65001 >nul
taskkill /f /im server.exe >nul 2>nul
timeout /t 2 >nul
exit

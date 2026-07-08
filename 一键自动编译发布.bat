@echo off
chcp 65001 >nul
echo ============================================================
echo [湖北项目] 一键自动编译与外网发布脚本
echo ============================================================

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0build.ps1"
pause

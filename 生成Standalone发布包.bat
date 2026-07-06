@echo off
chcp 65001 >nul
echo ============================================================
echo [湖北项目] 生成独立脱机版 (Standalone) 客户分发包
echo ============================================================

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0build_standalone.ps1"
pause

@echo off
chcp 65001 >nul
echo =======================================================
echo  湖北省公路事业发展中心 数据统筹治理平台
echo  养护统计年报智能体（独立版）
echo =======================================================
echo.
echo  [1/2] 正在启动本地数据服务（请勿关闭此窗口）...
echo  [2/2] 浏览器将自动打开年报助手...
echo.
echo  数据年份：2016 / 2017 / 2018 / 2019 / 2020
echo  默认展示：2016年度数据
echo.
echo  提示：关闭此黑色窗口后，数据查询功能将停止工作。
echo =======================================================
timeout /t 1 /nobreak >nul
start msedge "http://localhost:8000/index.html?mode=standalone&view=deepqa"
cd /d "%~dp0_app_env"
server.exe
pause

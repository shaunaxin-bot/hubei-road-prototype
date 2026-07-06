$ErrorActionPreference = 'Stop'
$releaseDir = 'C:\AIprojects\roaddata\hubei\release'
$standaloneDir = Join-Path $releaseDir 'standalone'
Write-Host '[1/4] Finding latest project directory...' -ForegroundColor Cyan
$projectDir = (Get-ChildItem -Path 'C:\AIprojects\roaddata\hubei' -Directory | Where-Object { $_.Name -match '^\d{8}$' } | Sort-Object Name -Descending | Select-Object -First 1).FullName
if (-not $projectDir) { Write-Host 'Error: Project directory not found!' -ForegroundColor Red; exit 1 }
Write-Host "Success: Found latest project: $projectDir" -ForegroundColor Green

Write-Host "`n[2/4] Initializing Standalone Sandbox..." -ForegroundColor Cyan
if (Test-Path $standaloneDir) { Remove-Item $standaloneDir -Recurse -Force }
New-Item -ItemType Directory -Path $standaloneDir | Out-Null
$srcHtml = (Get-ChildItem -Path $projectDir -Filter '*-hubei-prototype.html' | Select-Object -First 1).FullName
Copy-Item $srcHtml (Join-Path $standaloneDir 'index.html') -Force
Copy-Item (Join-Path $projectDir 'public') (Join-Path $standaloneDir 'public') -Recurse -Force
Write-Host "Success: Copied HTML and public folder" -ForegroundColor Green

Write-Host "`n[3/4] Compiling zero-dependency Python backend with PyInstaller (This may take 1-2 minutes)..." -ForegroundColor Cyan
Set-Location $projectDir
pyinstaller --onefile --distpath $standaloneDir --workpath (Join-Path $projectDir 'build') --specpath $projectDir server.py
Write-Host "Success: Backend compiled to server.exe!" -ForegroundColor Green

Write-Host "`n[4/4] Writing user-friendly startup batch script..." -ForegroundColor Cyan
$batPath = Join-Path $standaloneDir 'Run_Standalone.bat'
$batContent = @"
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
"@
Set-Content -Path $batPath -Value $batContent -Encoding UTF8
Write-Host "`nAll Done!" -ForegroundColor Green
Write-Host "Please package the directory $standaloneDir into a zip file and send it to the customer." -ForegroundColor Yellow

$ErrorActionPreference = 'Stop'
$date = Get-Date -Format 'yyyyMMdd'
$projectDir = (Get-ChildItem -Path 'C:\AIprojects\roaddata\hubei' -Directory | Where-Object { $_.Name -match '^\d{8}$' } | Sort-Object Name -Descending | Select-Object -First 1).FullName
$repoDir = 'C:\AIprojects\roaddata'
$ghRepoDir = 'C:\AIprojects\roaddata\hubei\release'

Write-Host '[1/5] Running QA tests...' -ForegroundColor Cyan
Set-Location $repoDir
python test_before_build.py
if ($LASTEXITCODE -ne 0) { 
    Write-Host '[ERROR] QA test failed, aborting release!' -ForegroundColor Red
    exit 1
}

Write-Host "`n[2/5] Compiling schemas and building UI..." -ForegroundColor Cyan
Set-Location $projectDir
python compile_public_schema.py
npm run build
python bundle_offline.py

$srcHtml = Join-Path $projectDir '20260705-hubei-prototype.html'

Write-Host "`n[3/5] Committing to Git..." -ForegroundColor Cyan
Set-Location $repoDir
git add -A
$msg = Read-Host 'Enter commit message (will add release: prefix)'
if ([string]::IsNullOrWhiteSpace($msg)) { $msg = 'auto release' }
git commit -m "release: hubei $date baseline - $msg"

Write-Host "`n[4/5] Copying to release directory..." -ForegroundColor Cyan
$releaseTarget = Join-Path $ghRepoDir 'index.html'
Copy-Item $srcHtml $releaseTarget -Force
Copy-Item (Join-Path $projectDir 'public\*.db') $ghRepoDir -Force
Copy-Item (Join-Path $projectDir 'public\sql-wasm.wasm') $ghRepoDir -Force
Write-Host "Done copying." -ForegroundColor Green

Write-Host "`n[5/5] Pushing to GitHub Pages..." -ForegroundColor Cyan
Set-Location $ghRepoDir
git add -A
git commit -m "Update Hubei release ($date)"
$env:GIT_TERMINAL_PROMPT = 0
git push origin main

Write-Host "`nRelease Finished Successfully!" -ForegroundColor Green

$ErrorActionPreference = 'Stop'
$date = Get-Date -Format 'yyyyMMdd'
$projectDir = (Get-ChildItem -Path 'C:\AIprojects\roaddata\hubei' -Directory | Where-Object { $_.Name -match '^\d{8}$' } | Sort-Object Name -Descending | Select-Object -First 1).FullName
$repoDir = 'C:\AIprojects\roaddata'
$ghRepoDir = 'C:\AIprojects\roaddata\hubei\release'
$projectDirName = Split-Path $projectDir -Leaf

$srcHtml = Join-Path $projectDir "$projectDirName-hubei-prototype.html"

Write-Host "`n[1/4] Compiling Knowledge Base Schemas & AIP Linkages..." -ForegroundColor Cyan
Set-Location $projectDir
python compile_public_schema.py
python compile_linkages.py
python compile_internal_linkages.py
python compile_ontology_lines.py

Write-Host "`n[2/4] Building Frontend and Generating Offline HTML..." -ForegroundColor Cyan
npm run build
python bundle_offline.py

Write-Host "`n[3/5] Committing to Git..." -ForegroundColor Cyan
Set-Location $repoDir
git add -A
$msg = Read-Host 'Enter commit message (will add release: prefix)'
if ([string]::IsNullOrWhiteSpace($msg)) { $msg = 'auto release' }
git commit -m "release: hubei $date baseline - $msg"

Write-Host "`n[4/5] Copying to release directory..." -ForegroundColor Cyan
$releaseTarget = Join-Path $ghRepoDir 'index.html'
Copy-Item $srcHtml $releaseTarget -Force
Remove-Item (Join-Path $ghRepoDir '*.db') -ErrorAction SilentlyContinue
Copy-Item (Join-Path $projectDir 'public\*.db') $ghRepoDir -Force
Copy-Item (Join-Path $projectDir 'public\*.html') $ghRepoDir -Force
Copy-Item (Join-Path $projectDir 'public\sql-wasm.wasm') $ghRepoDir -Force
if (Test-Path (Join-Path $projectDir 'public\images')) {
    Copy-Item (Join-Path $projectDir 'public\images') $ghRepoDir -Recurse -Force
    Remove-Item (Join-Path $ghRepoDir 'images\*.ppt') -ErrorAction SilentlyContinue
    Remove-Item (Join-Path $ghRepoDir 'images\*.pptx') -ErrorAction SilentlyContinue
    Remove-Item (Join-Path $ghRepoDir 'images\*.pdf') -ErrorAction SilentlyContinue
}
Write-Host "Done copying." -ForegroundColor Green

Write-Host "`n[5/5] Pushing to GitHub Pages..." -ForegroundColor Cyan
Set-Location $ghRepoDir
git add -A
git commit -m "Update Hubei release ($date)"
$env:GIT_TERMINAL_PROMPT = 0
git push origin main

Write-Host "`nRelease Finished Successfully!" -ForegroundColor Green

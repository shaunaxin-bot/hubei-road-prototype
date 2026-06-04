# Deploy script for GitHub Pages

git add index.html
git add ningbo\index.html
git commit -m "Update release prototype ($(Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))"
$env:GIT_TERMINAL_PROMPT=0
git push origin main
Write-Host "Deployed successfully to GitHub Pages!" -ForegroundColor Green

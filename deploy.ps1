# Deploy script for GitHub Pages

# Run build script
Write-Host "Running build..."
Start-Process -FilePath "C:\AIprojects\roaddata\ningbo\20260602\build.bat" -Wait -NoNewWindow

# Copy latest Ningbo prototype to release folder
Copy-Item -Path "C:\AIprojects\roaddata\ningbo\20260602\20260602-ningbo-prototype.html" -Destination "C:\AIprojects\roaddata\hubei\release\ningbo\index.html" -Force
Copy-Item -Path "C:\AIprojects\roaddata\ningbo\20260602\images" -Destination "C:\AIprojects\roaddata\hubei\release\ningbo" -Recurse -Force

git add -A
git commit -m "Update release prototype ($(Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))"
$env:GIT_TERMINAL_PROMPT=0
git push origin main
Write-Host "Deployed successfully to GitHub Pages!" -ForegroundColor Green


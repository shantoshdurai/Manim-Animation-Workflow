@echo off
setlocal enabledelayedexpansion

echo Calculating size and cleaning up Manim media folders...
powershell -ExecutionPolicy Bypass -Command "$mediaFolders = Get-ChildItem -Path . -Filter 'media' -Directory -Recurse | Where-Object { $_.FullName -notmatch 'portable_env' }; if ($mediaFolders) { $totalBytes = ($mediaFolders | Get-ChildItem -Recurse -File | Measure-Object -Property Length -Sum).Sum; if (!$totalBytes) { $totalBytes = 0 }; $totalMB = [Math]::Round($totalBytes / 1MB, 2); $mediaFolders | ForEach-Object { Write-Host 'Cleaning up: ' $_.FullName -ForegroundColor Cyan; Remove-Item -Path $_.FullName -Recurse -Force }; Write-Host ''; Write-Host ('Cleanup complete! You just saved ' + $totalMB + ' MB of space.') -ForegroundColor Green } else { Write-Host 'No media folders found. Everything is already clean!' -ForegroundColor Yellow }"
echo.
pause

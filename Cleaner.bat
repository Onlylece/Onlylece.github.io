@echo off
mode 1
title Cleaner by lece this will clean log,temp,RecycleBin
ipconfig /flushdns >nul 2>&1
echo Flushed DNS

del /s /f /q "C:\Windows\prefetch\*.*" >nul 2>&1
echo Prefetch Files Deleted

del /f /q "%localappdata%\temp\*" >nul 2>&1
rd /s /q "%WINDIR%\Temp" >nul 2>&1
echo Temp Files Deleted

del /f /q "%SystemRoot%\Traces\WindowsUpdate\*" >nul 2>&1
echo Windows Update Files Deleted

takeown /f "%temp%" /r /d y & RD /S /Q %temp% & MKDIR %temp% & takeown /f "%temp%" /r /d y & takeown /f "C:\Windows\Temp" /r /d y & RD /S /Q C:\Windows\Temp & MKDIR C:\Windows\Temp & takeown /f "C:\Windows\Temp" /r /d y

cd C:/ & del *.log /a /s /q /f

:: Empty Recycle Bin
PowerShell -ExecutionPolicy Unrestricted -Command "$bin = (New-Object -ComObject Shell.Application).NameSpace(10); $bin.items() | ForEach {; Write-Host "^""Deleting $($_.Name) from Recycle Bin"^""; Remove-Item $_.Path -Recurse -Force; }" >nul 2>&1
echo Recycle Bin Emptied
timeout 2 > nul
cls

echo Script Finished Cleaning Credits to lece#8088
timeout 3 > nul
cls
echo Press any key to exit...
pause > nul
exit
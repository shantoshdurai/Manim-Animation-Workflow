@echo off
set "VENV_PATH=c:\Manim\portable_env"
set "PATH=%VENV_PATH%\python;%VENV_PATH%\python\Scripts;%VENV_PATH%\ffmpeg;%VENV_PATH%\tinytex\TinyTeX\bin\windows;%PATH%"

if "%~1"=="" (
    echo Usage: Drag and drop a .py file onto this .bat file to render it.
    pause
    exit /b
)

echo.
echo ========================================
echo   MANIM PORTABLE RENDERER
echo ========================================
echo  [1] Low Quality    (480p,  15 fps) - Fast
echo  [2] Medium Quality (720p,  30 fps) - Balanced
echo  [3] High Quality   (1080p, 60 fps) - YouTube
echo  [4] 4K Quality     (2160p, 60 fps) - Best
echo ========================================
echo.

set /p choice="Choose quality (1-4) [Default is 1]: "

if "%choice%"=="2" (
    set "flag=-pqm"
) else if "%choice%"=="3" (
    set "flag=-pqh"
) else if "%choice%"=="4" (
    set "flag=-pqk"
) else (
    set "flag=-pql"
)

echo.
echo Rendering %~1 with %flag%...
python -m manim %flag% %~1
echo.
echo Done!
pause

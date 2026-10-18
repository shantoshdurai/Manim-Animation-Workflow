@echo off
setlocal enabledelayedexpansion

echo ========================================
echo   MANIM PORTABLE STUDIO SETUP (WINDOWS)
echo ========================================
echo This will download and set up Python 3.12, FFmpeg, and TinyTeX locally.
echo Everything will be self-contained within this folder.
echo.

set "ROOT=%~dp0"
set "ENV_DIR=%ROOT%portable_env"
set "TEMP_DIR=%ENV_DIR%\temp"

:: Create directories
if not exist "%ENV_DIR%" mkdir "%ENV_DIR%"
if not exist "%ENV_DIR%\python" mkdir "%ENV_DIR%\python"
if not exist "%ENV_DIR%\ffmpeg" mkdir "%ENV_DIR%\ffmpeg"
if not exist "%ENV_DIR%\tinytex" mkdir "%ENV_DIR%\tinytex"
if not exist "%TEMP_DIR%" mkdir "%TEMP_DIR%"

:: Download and configure Python
if not exist "%ENV_DIR%\python\python.exe" (
    echo [1/4] Downloading Python 3.12...
    powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.9/python-3.12.9-embed-amd64.zip' -OutFile '%TEMP_DIR%\python.zip'"
    echo Extracting Python...
    powershell -Command "Expand-Archive -Path '%TEMP_DIR%\python.zip' -DestinationPath '%ENV_DIR%\python' -Force"
    
    :: Enable site-packages
    powershell -Command "(Get-Content '%ENV_DIR%\python\python312._pth') -replace '#import site', 'import site' | Set-Content '%ENV_DIR%\python\python312._pth'"
    
    :: Install Pip
    echo Installing Pip...
    powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://bootstrap.pypa.io/get-pip.py' -OutFile '%TEMP_DIR%\get-pip.py'"
    "%ENV_DIR%\python\python.exe" "%TEMP_DIR%\get-pip.py"
) else (
    echo [1/4] Python is already installed.
)

:: Download FFmpeg
if not exist "%ENV_DIR%\ffmpeg\ffmpeg.exe" (
    echo [2/4] Downloading FFmpeg...
    powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip' -OutFile '%TEMP_DIR%\ffmpeg.zip'"
    echo Extracting FFmpeg...
    powershell -Command "Expand-Archive -Path '%TEMP_DIR%\ffmpeg.zip' -DestinationPath '%TEMP_DIR%\ffmpeg_extracted' -Force"
    for /d %%i in ("%TEMP_DIR%\ffmpeg_extracted\ffmpeg-*") do move "%%i\bin\*" "%ENV_DIR%\ffmpeg\"
) else (
    echo [2/4] FFmpeg is already installed.
)

:: Download TinyTeX
if not exist "%ENV_DIR%\tinytex\TinyTeX" (
    echo [3/4] Downloading TinyTeX (LaTeX)...
    powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://github.com/rstudio/tinytex-releases/releases/download/v2026.04/TinyTeX-v2026.04.zip' -OutFile '%TEMP_DIR%\tinytex.zip'"
    echo Extracting TinyTeX (This may take a few minutes)...
    powershell -Command "Expand-Archive -Path '%TEMP_DIR%\tinytex.zip' -DestinationPath '%ENV_DIR%\tinytex' -Force"
    
    :: Install required LaTeX packages
    echo Installing LaTeX packages (dvisvgm, preview, etc.)...
    set "PATH=%ENV_DIR%\tinytex\TinyTeX\bin\windows;%PATH%"
    call "%ENV_DIR%\tinytex\TinyTeX\bin\windows\tlmgr.bat" install dvisvgm standalone preview doublestroke geometry amsmath
) else (
    echo [3/4] TinyTeX is already installed.
)

:: Install Manim Community
echo [4/4] Installing Manim Community...
"%ENV_DIR%\python\python.exe" -m pip install --upgrade pip
"%ENV_DIR%\python\python.exe" -m pip install manim

:: Cleanup temporary folder
if exist "%TEMP_DIR%" rd /s /q "%TEMP_DIR%"

echo.
echo ========================================
echo   SETUP COMPLETE!
echo ========================================
echo You can now use render.bat and clean.bat.
echo.
pause

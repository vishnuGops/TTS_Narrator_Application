@echo off
echo Build folder cleanup
set distFolderPath=./dist

if exist "%distFolderPath%" (
    rmdir /s /q "%distFolderPath%"
    echo dist Folder deleted successfully.
) else (
    echo dist Folder does not exist.
)

set buildFolderPath=./build
if exist "%buildFolderPath%" (
    rmdir /s /q "%buildFolderPath%"
    echo Build folder deleted successfully.
) else (
    echo Build folder does not exist.
)

echo Building App Executable
pyinstaller --noconfirm --log-level=WARN --onefile --nowindow --icon=icon.ico ./TTS_app.py
echo Done building TTS Narration App

pause

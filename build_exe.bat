@echo off
echo === NC Simulator - Building EXE ===
echo.

REM Install PyInstaller if not installed
echo Installing PyInstaller...
pip install pyinstaller

echo.
echo Building executable...
echo This may take a few minutes...
echo.

REM Build single exe file
pyinstaller --onefile --windowed --name "NC_Simulator" main.py

echo.
echo ============================================
echo BUILD COMPLETE!
echo ============================================
echo.
echo EXE file location:
echo   dist\NC_Simulator.exe
echo.
echo You can copy this EXE to any Windows PC and run it
echo without installing Python!
echo.
pause

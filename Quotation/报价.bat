@echo off
REM Change to the directory of the script
cd /d "%~dp0"

REM Run the Python script
python "quotation.py"

REM Pause to keep the window open after execution
pause

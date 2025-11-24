@echo off
echo Starting AI Speech Evaluation System Backend...
echo.

if not exist venv (
    echo Error: Virtual environment not found!
    echo Please run setup.bat first
    pause
    exit /b 1
)

call venv\Scripts\activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

@echo off
echo ================================================
echo AI Speech Evaluation System - Backend Setup
echo ================================================
echo.

echo Step 1: Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error creating virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment created
echo.

echo Step 2: Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Error activating virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment activated
echo.

echo Step 3: Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed
echo.

echo Step 4: Downloading NLTK data...
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
if %errorlevel% neq 0 (
    echo Warning: NLTK download may have failed
)
echo ✓ NLTK data downloaded
echo.

echo Step 5: Creating .env file...
if not exist .env (
    copy .env.example .env
    echo ✓ .env file created from .env.example
) else (
    echo ✓ .env file already exists
)
echo.

echo ================================================
echo Setup complete!
echo ================================================
echo.
echo To start the server, run:
echo   venv\Scripts\activate
echo   uvicorn app.main:app --reload
echo.
pause

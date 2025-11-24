@echo off
echo ================================================
echo AI Speech Evaluation System - Frontend Setup
echo ================================================
echo.

echo Step 1: Installing dependencies...
call npm install
if %errorlevel% neq 0 (
    echo Error installing dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed
echo.

echo Step 2: Creating .env file...
if not exist .env (
    copy .env.example .env
    echo ✓ .env file created from .env.example
    echo.
    echo Please update .env with your backend URL if needed
) else (
    echo ✓ .env file already exists
)
echo.

echo ================================================
echo Setup complete!
echo ================================================
echo.
echo To start the development server, run:
echo   npm run dev
echo.
pause

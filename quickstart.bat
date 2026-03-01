@echo off
REM BhaashaGuru Quick Start Script for Windows
REM Run this script to set up and start the prototype

echo.
echo 🧠 BhaashaGuru - Multilingual STEM Tutor
echo ==========================================
echo.

REM Check Python version
echo Checking Python version...
python --version
echo.

REM Create virtual environment
echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated
echo.

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt > nul 2>&1
echo Dependencies installed
echo.

REM Check if .env exists
echo Checking configuration...
if not exist ".env" (
    echo WARNING: .env file not found!
    echo Creating .env from template...
    copy .env.example .env
    echo.
    echo Please edit .env and add your API key
    echo.
    echo Supported providers:
    echo - Groq (fastest free^): https://console.groq.com
    echo - HuggingFace (free^): https://huggingface.co/settings/tokens
    echo - OpenRouter (free^): https://openrouter.io
    echo.
    pause
) else (
    echo Configuration found
)
echo.

REM Run tests
echo Running tests...
echo.
python test_prototype.py
echo.
echo Tests completed!
echo.

REM Start the app
echo Starting Streamlit app...
echo.
echo The app will open in your browser at: http://localhost:8501
echo Press Ctrl+C to stop the app
echo.
echo ==========================================
echo.
streamlit run app.py

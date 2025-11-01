@echo off
REM Accessibility Learning Hub - Backend Setup Script for Windows

echo Setting up Accessibility Learning Hub Backend...

REM Check Python version
echo Checking Python version...
python --version

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

REM Download NLP models
echo Downloading NLP models...
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt

REM Create .env file if it doesn't exist
if not exist .env (
    echo Creating .env file...
    copy .env.example .env
    echo Please edit .env file with your credentials!
) else (
    echo .env file already exists
)

REM Create necessary directories
echo Creating directories...
if not exist uploads mkdir uploads
if not exist generated mkdir generated
if not exist temp mkdir temp
if not exist logs mkdir logs

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Edit .env file with your Firebase and API credentials
echo 2. Download Firebase Admin SDK credentials JSON
echo 3. Run: python app.py
echo.
echo API will be available at: http://localhost:5000
echo.

pause

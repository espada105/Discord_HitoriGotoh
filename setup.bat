@echo off
echo Starting Discord_HitoriGotoh bot installation...

REM 1. Clone Repository
if not exist "Discord_HitoriGotoh" (
    echo Cloning repository...
    git clone https://github.com/your_username/Discord_HitoriGotoh.git
    cd Discord_HitoriGotoh
) else (
    echo Repository already exists.
    cd Discord_HitoriGotoh
)

REM 2. Check FFmpeg
where ffmpeg >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo FFmpeg is not installed.
    echo Please install FFmpeg manually: https://ffmpeg.org/download.html
    pause
    exit
)

REM 3. Create Python Virtual Environment
echo Creating virtual environment...
python -m venv .venv

REM 4. Activate Virtual Environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM 5. Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM 6. Install Required Packages
echo Installing required packages...
pip install -U discord.py yt-dlp python-dotenv

REM 7. Create .env File
if not exist ".env" (
    set /p token="Please enter your Discord bot token: "
    echo DISCORD_BOT_TOKEN=%token%> .env
    echo .env file has been created.
) else (
    echo .env file already exists.
)

echo Installation complete!
echo To run the bot, use the following command:
echo python bot.py
pause
#!/bin/bash

echo "Starting Discord_HitoriGotoh bot installation..."

# 1. Clone Repository
if [ ! -d "Discord_HitoriGotoh" ]; then
    echo "Cloning repository..."
    git clone https://github.com/your_username/Discord_HitoriGotoh.git
    cd Discord_HitoriGotoh
else
    echo "Repository already exists."
    cd Discord_HitoriGotoh
fi

# 2. Check FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "FFmpeg is not installed."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        echo "Installing FFmpeg via Homebrew..."
        brew install ffmpeg
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        echo "Installing FFmpeg via apt..."
        sudo apt update
        sudo apt install -y ffmpeg
    fi
else
    echo "FFmpeg is already installed."
fi

# 3. Create Python Virtual Environment
echo "Creating virtual environment..."
python3 -m venv .venv

# 4. Activate Virtual Environment
echo "Activating virtual environment..."
source .venv/bin/activate

# 5. Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# 6. Install Required Packages
echo "Installing required packages..."
pip install -U discord.py yt-dlp python-dotenv

# 7. Create .env File
if [ ! -f ".env" ]; then
    echo "Please enter your Discord bot token: "
    read token
    echo "DISCORD_BOT_TOKEN=$token" > .env
    echo ".env file has been created."
else
    echo ".env file already exists."
fi

echo "Installation complete!"
echo "To run the bot, use the following command:"
echo "python bot.py"
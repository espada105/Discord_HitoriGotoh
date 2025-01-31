<div align="center">
  <img src="https://github.com/user-attachments/assets/adc8e7fc-e0b7-4280-858d-24165e509344" alt="봇치" width="300">
</div>

# Discord_HitoriGotoh: A Versatile Discord Music Bot

**Discord_HitoriGotoh** is a feature-rich Discord bot designed for playing music, managing queues, and providing an engaging experience for server members. This bot supports advanced music playback capabilities such as queue management, autoplay, and YouTube integration. It also includes slash commands for an intuitive user experience.

---

## 📜 Features

### 🎵 **Music Playback**
- **Play YouTube Videos**: Play audio directly from YouTube links.
- **Queue Management**: Add songs to the queue and manage the playback order.
- **Autoplay**: Automatically play recommended videos when the queue is empty.
- **Skip Songs**: Skip to the next song in the queue.
- **Custom Song Commands**: Easily play pre-defined favorite songs with commands.

### 🔧 **Slash Commands**
- **/재생**: Play a song using a YouTube URL.
- **/대기열**: View the current music queue.
- **/나가기**: Disconnect the bot from the voice channel.
- **/무리**: Automatically play a predefined song.
- **/자동재생**: Toggle autoplay (YouTube recommendations).

---


# Setup Guide for Discord_HitoriGotoh Bot

This repository contains two setup scripts for installing the Discord_HitoriGotoh bot on different operating systems.

## 📋 Prerequisites

Before running the setup scripts, ensure you have:
- Git installed
- Python 3.8 or higher installed
- Discord Bot Token ready
- Administrator privileges (for Linux/macOS)

## 🛠️ Setup Scripts

### Windows Users (`setup.bat`)

1. **Download the Script**
   - Save `setup.bat` to your desired installation directory

2. **Run the Script**
   ```batch
   setup.bat
   ```
   Or double-click the file in Windows Explorer

### Linux/macOS Users (`setup.sh`)

1. **Download the Script**
   - Save `setup.sh` to your desired installation directory

2. **Make the Script Executable**
   ```bash
   chmod +x setup.sh
   ```

3. **Run the Script**
   ```bash
   ./setup.sh
   ```

## 🔄 What the Scripts Do

Both scripts perform the following automated tasks:

1. **Repository Setup**
   - Clones the Discord_HitoriGotoh repository
   - Changes to the project directory

2. **FFmpeg Installation**
   - Checks for FFmpeg installation
   - Windows: Provides download link if not installed
   - Linux/macOS: Automatically installs via package manager

3. **Python Environment**
   - Creates a virtual environment (.venv)
   - Activates the virtual environment
   - Upgrades pip to latest version

4. **Dependencies**
   - Installs required Python packages:
     - discord.py
     - yt-dlp
     - python-dotenv

5. **Configuration**
   - Creates .env file
   - Prompts for Discord bot token
   - Saves token to .env file

## ⚠️ Troubleshooting

### Common Issues

1. **Permission Denied**
   ```bash
   # Linux/macOS
   sudo chmod +x setup.sh
   ```

2. **FFmpeg Not Found**
   - Windows: Download manually from [FFmpeg website](https://ffmpeg.org/download.html)
   - Linux: `sudo apt install ffmpeg`
   - macOS: `brew install ffmpeg`

3. **Python Not Found**
   - Ensure Python is installed and added to PATH
   - Try using `python3` instead of `python` on Linux/macOS

## 📝 Post-Installation

After successful installation:

1. Verify installation:
   ```bash
   python bot.py
   ```

2. The bot should show as online in your Discord server

3. Test basic commands like `/재생` or `/대기열`

## 🔄 Updating

To update the bot:

1. Delete the existing installation
2. Run the setup script again

## 💡 Additional Notes

- Keep your Discord bot token secure
- Don't share your .env file
- Regular updates are recommended
- Check GitHub releases for latest versions
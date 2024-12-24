<div align="center">
  <img src="https://github.com/user-attachments/assets/adc8e7fc-e0b7-4280-858d-24165e509344" alt="봇치" width="300">
</div>

# Discord_HitoriGotoh: A Versatile Discord Music Bot

**Discord_HitoriGotoh** is a feature-rich Discord bot designed for playing music, managing queues, and providing an engaging experience for server members. This bot supports advanced music playback capabilities such as queue management, autoplay, and YouTube integration. It also includes slash commands for an intuitive user experience.

---

## Features

### 🎵 Music Playback
- **Play YouTube Videos**: Play audio directly from YouTube links.
- **Queue Management**: Add songs to the queue and manage the playback order.
- **Autoplay**: Automatically play recommended videos when the queue is empty.
- **Skip Songs**: Skip to the next song in the queue.
- **Custom Song Commands**: Easily play pre-defined favorite songs with commands.

### 🔧 Slash Commands
- **/재생**: Play a song using a YouTube URL.
- **/대기열**: View the current music queue.
- **/나가기**: Disconnect the bot from the voice channel.
- **/무리**: Automatically play a predefined song.
- **/자동재생**: Toggle autoplay (YouTube recommendations).
- **/control**: Display an interactive music controller.

### ⚡ Interactive Features
- **Interactive Buttons**: Skip songs using a Discord button-based interface.
- **Terminal Control**: Control and monitor the bot from your terminal.

### 🛠️ Robust Integration
- **YouTube Integration**: Fetch YouTube videos using the `yt_dlp` library.
- **Discord Slash Commands**: Fully integrated with Discord’s modern slash command interface.
- **Dynamic Queue Playback**: Ensures seamless transitions between queued songs.

---

## Installation

### Prerequisites
- Python 3.8+
- Discord Developer Bot Token
- FFmpeg installed and added to PATH
- `yt-dlp` library

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/Discord_HitoriGotoh.git
   cd Discord_HitoriGotoh

import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import yt_dlp

# 환경 변수 로드
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# 봇 설정
class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        self.queue = []  # 대기열
        self.auto_play = True  # 자동 재생 설정

    async def setup_hook(self):
        await self.tree.sync()

bot = MyBot()
# 음악 재생 함수
async def play_music(interaction, video_url):
    try:
        await interaction.response.defer()  # 작업 진행 중임을 알림
        user = interaction.user
        if not user.voice or not user.voice.channel:
            await interaction.followup.send("ㅁ..먼저 음성 채널에 들어가 주ㅅ..세요!")
            return

        channel = user.voice.channel
        if interaction.guild.voice_client is None:
            voice_client = await channel.connect()
        else:
            voice_client = interaction.guild.voice_client

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            audio_url = info['url']
            if voice_client.is_playing():
                bot.queue.append((info['title'], audio_url, info))
                await interaction.followup.send(f"대기열에 추가: {info['title']}")
            else:
                voice_client.play(discord.FFmpegPCMAudio(audio_url), after=lambda e: bot.loop.create_task(play_next(interaction, info)))
                await interaction.followup.send(f"재생 중: {info['title']}")
    except Exception as e:
        await interaction.followup.send(f"오류 발생: {e}")

# 슬래시 명령어: 노래 검색 및 재생
@bot.tree.command(name="재생", description="봇치가 유튜브 URL을 보고 노래를 연주합니다.")
async def play(interaction: discord.Interaction, url: str):
    await play_music(interaction, url)


# 대기열에서 다음 곡 재생
async def play_next(interaction, current_info=None):
    if bot.queue:
        next_title, next_audio, next_info = bot.queue.pop(0)
        voice_client = interaction.guild.voice_client
        if voice_client:
            voice_client.play(discord.FFmpegPCMAudio(next_audio), after=lambda e: bot.loop.create_task(play_next(interaction)))
            channel = interaction.channel
            await channel.send(f"다음 곡 재생 중: {next_title}")
    elif bot.auto_play and current_info:
        # 유튜브 추천 동영상 가져오기
        next_video_url = get_next_video_url(current_info)
        if next_video_url:
            await play_music(interaction, next_video_url)
    else:
        voice_client = interaction.guild.voice_client
        if voice_client:
            await voice_client.disconnect()
            channel = interaction.channel
            await channel.send("대기열이 비어 있어 봇치가 도망갔습니다.")

# 유튜브 추천 동영상 가져오기
def get_next_video_url(current_info):
    try:
        related_videos = current_info.get('related_videos', [])
        if related_videos:
            return f"https://www.youtube.com/watch?v={related_videos[0]['id']}"  # 첫 번째 추천 영상
    except Exception as e:
        print(f"추천 동영상 가져오기 오류: {e}")
    return None


# 슬래시 명령어: 특정 곡 자동 재생
@bot.tree.command(name="무리", description="특정 노래를 자동으로 재생합니다.")
async def play_muri(interaction: discord.Interaction):
    video_url = "https://www.youtube.com/watch?v=cPvrGYNxBlg"
    await play_music(interaction, video_url)

# 슬래시 명령어: 대기열 확인
@bot.tree.command(name="대기열", description="현재 대기열을 출력합니다.")
async def show_queue(interaction: discord.Interaction):
    if not bot.queue:
        await interaction.response.send_message("대기열이 비어 있습니다!")
    else:
        queue_list = "\n".join([f"{idx+1}. {title}" for idx, (title, _, _) in enumerate(bot.queue)])
        await interaction.response.send_message(f"현재 대기열:\n{queue_list}")

# 슬래시 명령어: 음성 채널 나가기
@bot.tree.command(name="나가기", description="봇이 음성 채널에서 나갑니다.")
async def leave(interaction: discord.Interaction):
    if interaction.guild.voice_client:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("봇치가 도망갔습니다.")
    else:
        await interaction.response.send_message("봇치가 음성 채널에 있지 않습니다.")

# 슬래시 명령어: 자동 재생 설정 변경
@bot.tree.command(name="자동재생", description="자동 재생 설정을 켜거나 끕니다.")
async def toggle_auto_play(interaction: discord.Interaction, 상태: str):
    if 상태.lower() == "켜기":
        bot.auto_play = True
        await interaction.response.send_message("자동 재생이 활성화되었습니다!")
    elif 상태.lower() == "끄기":
        bot.auto_play = False
        await interaction.response.send_message("자동 재생이 비활성화되었습니다!")
    else:
        await interaction.response.send_message("사용법: /자동재생 켜기 또는 /자동재생 끄기")

# 봇 상태 변경
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="봇치는 성인이와 연주"))
    print(f"봇치가 등장했습니다: {bot.user}")

# 봇 실행
bot.run(TOKEN)

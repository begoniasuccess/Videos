import os
import yt_dlp

# ========= 設定 =========
BASE_DIR = r"C:/Users/USER/Desktop/WhiteNoisePlaylist"  # 修改成你要的路徑
AUDIO_FORMAT = "m4a"

# 各時段影片連結
PLAYLISTS = {
    "morning": [
        "https://www.youtube.com/watch?v=EHklxmBvzwc",
        "https://www.youtube.com/watch?v=xN_9Nqamp_g",
        "https://www.youtube.com/watch?v=F1gK85IEeDI",
        "https://www.youtube.com/watch?v=2LMqOdCHQWw",
        "https://www.youtube.com/watch?v=PL705M_3KOY",
        "https://www.youtube.com/watch?v=mByYP4Lh4dM",
    ],
    "noon": [
        "https://www.youtube.com/watch?v=WHPEKLQID4U",
        "https://www.youtube.com/watch?v=JekUNGo-RVk",
        "https://www.youtube.com/watch?v=j1lLwUBkOAg",
        "https://www.youtube.com/watch?v=edNd4cI1eLw",
        "https://www.youtube.com/watch?v=uY7l_4unbnE",
    ],
    "afternoon": [
        "https://www.youtube.com/watch?v=h2zkV-l_TbY",
        "https://www.youtube.com/watch?v=uiMXGIG_DQo",
        "https://www.youtube.com/watch?v=Apygp914NI4",
        "https://www.youtube.com/watch?v=jko0E76Xmfc",
        "https://www.youtube.com/watch?v=137eJvRA_IA",
    ],
    "night": [
        "https://www.youtube.com/watch?v=iRUfxVLBH5k",
        "https://www.youtube.com/watch?v=E77jmtut1Zc",
        "https://www.youtube.com/watch?v=EUCzn76UFE0",
        "https://www.youtube.com/watch?v=dVpZEIpl4-w",
        "https://www.youtube.com/watch?v=xEytkJtDUZQ",
    ],
    "midnight": [
        "https://www.youtube.com/watch?v=iEy9BXGs2R4",
        "https://www.youtube.com/watch?v=JekUNGo-RVk",
        "https://www.youtube.com/watch?v=bn9F19Hi1Lk",
        "https://www.youtube.com/watch?v=iP_Go9SqU5E",
        "https://www.youtube.com/watch?v=AgpWX18dby4",
        "https://www.youtube.com/watch?v=nMfPqeZjc2c",
        "https://www.youtube.com/watch?v=2sDZn83ZFfI",
        "https://www.youtube.com/watch?v=Og40mpl8VNc",
        "https://www.youtube.com/watch?v=CN_W_UW6S_0",
        "https://www.youtube.com/watch?v=pKAvj-D8naU",
    ],
}

# ========= 主要程式 =========
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def download_audio(url, out_dir):
    opts = {
        "format": f"bestaudio[ext={AUDIO_FORMAT}]/bestaudio/best",
        "outtmpl": os.path.join(out_dir, "%(title)s.%(ext)s"),
        "quiet": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": AUDIO_FORMAT,
        }],
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])

def main():
    ensure_dir(BASE_DIR)
    txt_lines = []
    m3u_lines = ["#EXTM3U\n"]

    for period, urls in PLAYLISTS.items():
        folder = os.path.join(BASE_DIR, period)
        ensure_dir(folder)
        print(f"\n🎧 下載 {period} 時段 ({len(urls)} 條)...")

        for url in urls:
            try:
                download_audio(url, folder)
                txt_lines.append(f"{period}: {url}\n")
                m3u_lines.append(os.path.join(folder, f"{url}\n"))
            except Exception as e:
                print(f"❌ 無法下載 {url}: {e}")

    # 輸出播放清單
    with open(os.path.join(BASE_DIR, "playlist.txt"), "w", encoding="utf-8") as f:
        f.writelines(txt_lines)
    with open(os.path.join(BASE_DIR, "playlist.m3u"), "w", encoding="utf-8") as f:
        f.writelines(m3u_lines)

    print("\n✅ 全部下載完成！播放清單已建立。")

if __name__ == "__main__":
    main()

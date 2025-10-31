import yt_dlp

def download_playlist(playlist_url, output_template="python/Economics/%(playlist_index)s_%(title)s.%(ext)s"):
    ydl_opts = {
        # 'format': 'best',  # 選擇最佳畫質
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # 選擇最高畫質影片和音訊
        'outtmpl': output_template,  # 定義每個影片的下載文件名稱
        'noplaylist': False,  # 指定下載整個播放清單
        # 'playliststart': 5,   # 從第 n 個影片開始
        # 'playlistend': 6   # 在第 n 個影片結束
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

playlist_url = 'https://youtube.com/playlist?list=PLCX-BLZ1hDpB8NQC4lwIsn9CJVVMHUIY-&si=TZJ2FZfIy-dbfNvP'
download_playlist(playlist_url)
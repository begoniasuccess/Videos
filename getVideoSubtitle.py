import moviepy.editor as mp
import whisper

def extract_audio(video_path, audio_path):
    """從影片中提取音訊"""
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def transcribe_audio(audio_path, output_srt):
    """轉譯音訊為帶時間軸的字幕"""
    model = whisper.load_model("base")  # 可選 "base", "small", "medium", "large"
    result = model.transcribe(audio_path, task="transcribe")

    # 將結果儲存為 SRT 格式
    with open(output_srt, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result['segments']):
            start = segment['start']
            end = segment['end']
            text = segment['text']
            
            # 格式化時間軸
            start_time = format_timestamp(start)
            end_time = format_timestamp(end)
            f.write(f"{i + 1}\n{start_time} --> {end_time}\n{text.strip()}\n\n")

def format_timestamp(seconds):
    """將時間秒數轉換為 SRT 格式 (hh:mm:ss,ms)"""
    millis = int((seconds % 1) * 1000)
    seconds = int(seconds)
    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

if __name__ == "__main__":
    video_path = r"D:\Begonia\study\SMT\video\CH-11-1.mp4"  # 替換為你的影片檔路徑
    audio_path = "CH-11-1.wav"
    output_srt = "CH-11-1.srt"

    extract_audio(video_path, audio_path)
    transcribe_audio(audio_path, output_srt)
    print(f"字幕已保存到 {output_srt}")

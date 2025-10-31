import subprocess
import os

def compress_video(input_file, output_file, bitrate="500k"):
    """
    壓縮影片檔案大小
    :param input_file: 原影片檔案路徑
    :param output_file: 壓縮後影片檔案路徑
    :param bitrate: 壓縮後的目標比特率 (預設 500k)
    
    
    """
    if not os.path.exists(input_file):
        print(f"找不到檔案：{input_file}")
        return
    
    # FFmpeg 命令
    command = [
        "ffmpeg",
        "-i", input_file,
        "-b:v", bitrate,  # 設置影片比特率
        "-b:a", "128k",   # 設置音訊比特率
        "-preset", "fast", # 壓縮速度（可選 slow、fast 等）
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"壓縮完成！輸出檔案：{output_file}")
    except subprocess.CalledProcessError as e:
        print(f"壓縮失敗：{e}")
    except FileNotFoundError:
        print("請確認 FFmpeg 是否已安裝並配置至環境變數中！")

def process_mp4_files(folder_path):
    # 1. 遍歷資料夾並取得所有 mp4 檔案名稱
    mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4') or f.endswith('.MP4')]

    # 2. 確認是否存在 compressVideo 子資料夾，若無則創建
    compress_folder_path = os.path.join(folder_path, 'compressVideo')
    if not os.path.exists(compress_folder_path):
        os.makedirs(compress_folder_path)
        print(f"Created 'compressVideo' folder at {compress_folder_path}")

    # 3. 遍歷每個 mp4 檔案並處理
    for mp4_file in mp4_files:
        input_path = os.path.join(folder_path, mp4_file)
        
        # 4. 從 input_path 汲取名稱和副檔名部分
        video_name = os.path.basename(input_path)
        
        # 5. 設定 output_path 為 compressVideo 子資料夾的路徑加上 video_name
        output_path = os.path.join(compress_folder_path, video_name)
        
        # 6. 檢查 output_path 指向的檔案是否存在，若存在則跳過
        if os.path.exists(output_path):
            print(f"File already exists: {output_path}, skipping.")
            continue
        
        # 7. 執行壓縮函式
        compress_video(input_path, output_path, bitrate="300k")

# 使用示範資料夾路徑
if __name__ == '__main__':
    folder_path = f"../../electronic_circuit"
    process_mp4_files(folder_path)

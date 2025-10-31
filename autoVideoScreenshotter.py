from moviepy.editor import VideoFileClip
import os

print("===開始===")

# 設定影片路徑和儲存圖片的資料夾
folder_path = 'Chemical/高中全部/'
output_folder = 'screenshots/chemical'
os.makedirs(output_folder, exist_ok=True)

# 遍歷資料夾
for filename in os.listdir(folder_path):
    
    # --- 檢查是否為 .mp4 檔案且檔名包含「錯合物」
    if not (filename.endswith('.mp4') and '錯合物' in filename):
        continue
    
    video_path = os.path.join(folder_path, filename)
    print(video_path)

    # --- 開始截圖
    # # 加載影片        
    # clip = VideoFileClip(video_path)

    # # 每3秒截圖一次
    # screenshot_count = 0
    # video_name = os.path.splitext(os.path.basename(filename))[0]

    # print("開始截圖...")
    
    # for t in range(0, int(clip.duration), 3):
    #     screenshot_path = os.path.join(output_folder, f'{video_name}_{screenshot_count}.jpg')
    #     clip.save_frame(screenshot_path, t)
    #     screenshot_count += 1

    # print("截圖完成！")
    
print("===結束===")
    

        
    

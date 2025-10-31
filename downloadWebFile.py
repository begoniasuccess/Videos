import os
import requests

# 定義要存放檔案的資料夾
output_dir = r"D:\Begonia\study\SMT\video"

# 確保資料夾存在
os.makedirs(output_dir, exist_ok=True)

# 要下載的影片連結
urls = [
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-11-2.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-11-3.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-12-1.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-12-2.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-13.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-14-1.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-14-2.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-15.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-16-1.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-16-2.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-16-3.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-17-1.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-17-2.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-17-3.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-18-1.mp4",
    "https://e3p.nycu.edu.tw/pluginfile.php/211681/mod_folder/content/0/CH-18-2.mp4"
]

# 下載每個檔案
for url in urls:
    file_name = url.split("/")[-1]
    output_path = os.path.join(output_dir, file_name)
    
    try:
        print(f"正在下載 {file_name}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 確保請求成功
        
        # 將內容寫入檔案
        with open(output_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"{file_name} 下載完成！")
    except requests.RequestException as e:
        print(f"下載 {file_name} 時發生錯誤: {e}")

print("所有檔案下載完成！")

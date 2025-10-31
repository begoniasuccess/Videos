from pytube import Playlist

playLists = [
    # "https://youtube.com/playlist?list=PL1h3qelyoklCqu1yPXaNGciZXQumNrK7c&si=pGmtF5i7hfO7kWJn",
    # "https://youtube.com/playlist?list=PL1h3qelyoklBj20ZMlT_Nzac_EGn-5yHF&si=XjHzg8u1zvBKeE_8",
    "https://youtube.com/playlist?list=PLjD5U4qWtDY4oTbUkIV2GlObmhb5DbAy9&si=o2AlP52f383zkoYC",
]

video_urls = []

for playlist_url in playLists:
    # 建立 Playlist 物件
    pl = Playlist(playlist_url)

    # pytube 的 Playlist 會自動擷取所有影片URL
    print(f"找到 {len(pl.video_urls)} 部影片：")

    for url in pl.video_urls:
        video_urls.append(url)

html_head = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>YT Video Preview</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        .avideo{
            position: relative;
            width: 100%;
            padding-bottom: 56.25%; /* 16:9 的高寬比 */
            height: 0;
            margin: 2em 0 ;
        }
        .avideo iframe {
            position: absolute;
            width: 100%;
            height: 100%;
            left: 0;
            top: 0;
        }
    </style>
</head>
<body>
<h1>YT Video Preview</h1>
"""

html_body = ""
for url in video_urls:
    if "watch?v=" in url:
        video_id = url.split("watch?v=")[-1]
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[-1]
    else:
        continue
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    html_body += f'<div class="avideo"><iframe width="560" height="315" src="{embed_url}" frameborder="0" allowfullscreen></iframe></div>\n'

html_footer = """
<div style="height:500px;"></div>
</body>
</html>
"""

with open("yt_preview.html", "w", encoding="utf-8") as f:
    f.write(html_head + html_body + html_footer)

print("HTML 預覽頁面已產生：yt_preview.html")

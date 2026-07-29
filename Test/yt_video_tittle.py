from yt_dlp import YoutubeDL

video_id = "yUFpTtM7PvI"

try:
    with YoutubeDL({"quiet": True}) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)

    title = info["title"]
    print( type(title) )

except Exception as e:
    print( type(e).__name__ )
    print(e)
import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s' # Save as title of video
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

download_video("https://reeelapps-app.s3.us-west-2.amazonaws.com/contentreelai-render/889/10151/output.mp4")

import youtube_dl
def download_ytvid_as_mp3():
    video_url = input("enrez l'url de la vidéo :\n")
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':"..\\mp3\\"+filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("\nDownload complete... {}".format(filename))
download_ytvid_as_mp3()

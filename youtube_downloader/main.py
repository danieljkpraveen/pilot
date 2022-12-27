import re
from pytube import YouTube, Playlist


def download_video(link):
    ytObj = YouTube(link)
    ytObj = ytObj.streams.get_highest_resolution()
    try:
        ytObj.download()
        print("\n✅ Download Completed\n")
    except Exception as e:
        print("\n❎ Download Failed\n")


def download_audio(link, name):
    name = name+'.mp3'
    print(name)
    ytObj = YouTube(link)
    ytObj = ytObj.streams.get_audio_only()
    try:
        ytObj.download(filename=name)
        print("\n✅ Download Completed\n")
    except Exception as e:
        print(e)
        print("\n❎ Download Failed\n")
    

def download_playlist(link):
    download_path = 'D:\\youtube_download'
    playlist = Playlist(link)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    for video in playlist.videos:
        video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(download_path)


if __name__ == '__main__':
    link = input("Enter link ▶ ")
    choice = True
    while choice:
        option = int(input("1. Download Video\n2. Download Audio\n3. Download Playlist\n4. Quit\nEnter Choice ▶ "))
        if (option == 1):
            download_video(link)
        elif (option == 2):
            name = input("Enter Filename ▶ ")
            download_audio(link, name)
        elif (option == 3):
            download_playlist(link)
        elif (option == 4):
            choice = Falsee
        else:
            print("Invalid Option")


from pytube import *


def download_by_name(folder):
    """ Download song by name """

    song = input("Enter the song name: ")

    if song:
        try:
            yt_search = Search(song)
            print("[+] Searching...")

            first_result = str(yt_search.results[0])
            id_video = first_result[41:52]

            url_video = f"https://youtu.be/{id_video}"

            yt_video = YouTube(url_video)
            print(f"[+] {yt_video.title} found!")

            # Dowload the video
            print(f"[+] {yt_video.title} will be downloaded")
            seted_video = yt_video.streams.get_by_itag(18)
            seted_video.download(folder)
            print(f"[+] {yt_video.title} Downloaded!")

        except Exception as error:
            print(f"[-] Has been an error: {error}")

    else:
        print("[-] You must enter a song name")

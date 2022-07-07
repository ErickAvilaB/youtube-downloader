""" Downloader module """
from pytube import *


def download(song_name, folder):
    """ Basic download preocess """
    try:
        yt_search = Search(song_name)
        print("[+] Searching...")

        first_result = str(yt_search.results[0])
        id_video = first_result[41:52]

        url_video = f"https://youtu.be/{id_video}"

        yt_video = YouTube(url_video)
        print(f"[+] {yt_video.title} found and will be downloaded")

        # Dowload the video
        stream = yt_video.streams.get_by_itag(140)
        stream.download(folder)
        print(f"[+] {yt_video.title} Downloaded!")

    except Exception as error:
        print(f"[-] Has been an error: {error}")

    print("[    -----    ]")


def download_by_name(folder):
    """ Download song by name """
    song_input = input("[+] Enter the song name: ")

    if song_input:
        download(song_input, folder)

    else:
        print("[!] You must enter a song name")


def download_by_tracklist(path_tracklist_file, folder):
    """ Download by tracklist """
    with open(path_tracklist_file, "r") as file:
        tracklist = file.readlines()

    if tracklist:
        for track in tracklist:
            download(track, folder)

    elif not tracklist:
        print("[-] Tracklist is empty")

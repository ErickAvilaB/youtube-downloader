""" Downloader module """
import re
from pytube import YouTube, Search


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

    finally:
        print("[    -----    ]")


def download_by_url(folder):
    """ Download by url """
    while True:
        song_input = input(
            "[+] Enter the url with format (youtu.be/) or (youtube.com/watch?v=). (q) to back: ")

        validate = re.search("https://youtu.be/", song_input)
        validate_2 = re.search("https://www.youtube.com/watch?", song_input)

        if not song_input:
            print("[!] You must enter a url")

        elif song_input == "q":
            break

        elif (validate is None) and (validate_2 is None):
            print("[!] Invalid url")

        elif (validate is not None) or (validate_2 is not None):
            try:
                yt_video = YouTube(song_input)
                print(f"[+] {yt_video.title} found and will be downloaded")

                # Dowload the video
                stream = yt_video.streams.get_by_itag(140)
                stream.download(folder)
                print(f"[+] {yt_video.title} Downloaded!")

            except Exception as error:
                print(f"[-] Has been an error: {error}")

            finally:
                print("[    -----    ]")


def download_by_name(folder):
    """ Download song by name """
    while True:
        song_input = input("[+] Enter the song name. (q) to back: ")

        if not song_input:
            print("[!] You must enter a song name")

        elif song_input == "q":
            break

        else:
            download(song_input, folder)


def download_by_tracklist(path_tracklist_file, folder):
    """ Download by tracklist """
    with open(path_tracklist_file, "r", encoding="utf-8") as file:
        tracklist = file.readlines()

    if tracklist:
        for track in tracklist:
            download(track, folder)

    elif not tracklist:
        print("[-] Tracklist is empty")

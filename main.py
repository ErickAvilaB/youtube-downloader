from pytube import *
from os import system
from change_symbols import remove_symbols


def main():
    "Search the video by name"
    yt_search = Search("Mac Miller - Congratularions")
    print("[+] Searching...")

    "Take the video id of the first result"
    first_result = str(yt_search.results[0])
    id_video = first_result[41:52]
    "Create an ulr whit the video id"
    url_video = f"https://www.youtubepp.com/watch?v={id_video}"

    yt_video = YouTube(url_video)
    print(f"[+] {yt_video.title} found!")

    "Download the video filtered by mp4"
    st = yt_video.streams.get_by_itag("139")
    st.download()
    print(f"[+] {yt_video.title} Downloaded!")

    "Convert the video to mp3"
    command_to_mp3 = "ffmpeg -i " + \
        remove_symbols(yt_video.title) + ".mp4 " + \
        remove_symbols(yt_video.title) + ".mp3"
    system(command_to_mp3)
    print(f"[+] {yt_video.title} converted to mp3!")

    "Delete the video"
    command_to_remove = "rm " + remove_symbols(yt_video.title) + ".mp4"
    system(command_to_remove)
    print(f"[+] {yt_video.title} removed!")


if __name__ == "__main__":
    main()

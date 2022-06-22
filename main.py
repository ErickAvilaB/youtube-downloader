from pytube import *


def main():
    """ Search the video by name and take the first_result, then create the url_video """
    yt_search = Search("MBDTF - Kanye West")
    print("[+] Searching...")

    first_result = str(yt_search.results[0])
    id_video = first_result[41:52]

    url_video = f"https://www.youtube.com/watch?v={id_video}"

    yt_video = YouTube(url_video)
    print(f"[+] {yt_video.title} found!")

    # Dowload the video
    seted_video = yt_video.streams.get_by_itag(139)
    seted_video.download()
    print(f"[+] {yt_video.title} Downloaded!")


if __name__ == "__main__":
    main()

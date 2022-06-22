import os
from pytube import *
from moviepy.editor import *


def convert_to_mp3(folder):
    """ Convert videos to mp3 """
    downloads_folder = os.path.join(folder, "downloads")
    for file in os.listdir(downloads_folder):
        if file.endswith(".mp4"):
            mp4_file_path = os.path.join(downloads_folder, file)
            mp3_file_path = os.path.join(downloads_folder, file[:-4] + ".mp3")

            video = VideoFileClip(mp4_file_path)
            video.audio.write_audiofile(mp3_file_path)

            print(f"[+] {mp4_file_path} converted to {mp3_file_path}")

            os.remove(mp4_file_path)
            print(f"[+] {mp4_file_path} removed")


def main():
    """ Search the video by name and take the first_result, then create the url_video """
    yt_search = Search("Everybody Mac Miller")
    print("[+] Searching...")

    first_result = str(yt_search.results[0])
    id_video = first_result[41:52]

    url_video = f"https://www.youtube.com/watch?v={id_video}"

    yt_video = YouTube(url_video)
    print(f"[+] {yt_video.title} found!")

    # Dowload the video
    # print(yt_video.streams.filter(file_extension='mp4'))
    seted_video = yt_video.streams.get_by_itag(18)
    seted_video.download("/home/erick/workspace/youtube/downloads")
    print(f"[+] {yt_video.title} Downloaded!")


if __name__ == "__main__":
    main()
    convert_to_mp3("/home/erick/workspace/youtube")

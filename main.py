import os
from time import sleep
from pytube import *
from moviepy.editor import *


downloads_folder = os.path.join(os.getcwd(), "downloads")

try:
    os.mkdir(downloads_folder)

except FileExistsError:
    pass


def convert_downloads_to_mp3(**folderKey):
    """ Decorator to convert mp4 downloaded files to mp3 """
    def decorator(function):
        def wrapper(**kwargs):
            function(**kwargs)

            print("[~] Let's convert all downloads folder mp4 files to mp3")
            sleep(1.5)
            for file in os.listdir(folderKey["content"]):
                if file.endswith(".mp4"):
                    mp4_file_path = os.path.join(folderKey["content"], file)
                    mp3_file_path = os.path.join(
                        folderKey["content"], file[:-4] + ".mp3")

                    video = VideoFileClip(mp4_file_path)
                    video.audio.write_audiofile(mp3_file_path)

                    print(
                        f"[~] {mp4_file_path[40:]} converted to {mp3_file_path[40:]}")

                    os.remove(mp4_file_path)
                    print(f"[~] {mp4_file_path[40:]} removed")
        return wrapper
    return decorator


@convert_downloads_to_mp3(content=downloads_folder)
def main(**kwargs):
    """ Search the video by name and take the first_result then download it """
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
            seted_video.download(kwargs["folderForDownloads"])
            print(f"[+] {yt_video.title} Downloaded!")

        except Exception as e:
            print(f"[-] Has been an error: {e}")

    else:
        print("[-] You must enter a song name")


if __name__ == "__main__":
    main(folderForDownloads=downloads_folder)

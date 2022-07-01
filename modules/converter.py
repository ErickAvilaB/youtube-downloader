import os
from moviepy.editor import *
from time import sleep


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

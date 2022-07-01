""" Converter module """
import os
from moviepy.editor import *


def convert_mp4_to_mp3(downloaded_content):
    """ Decorator to convert mp4 downloaded files to mp3 """
    def decorator(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)

            list_files = os.listdir(downloaded_content)
            if list_files:
                print("[~] Let's convert all downloads folder mp4 files to mp3")
                for file in list_files:
                    if file.endswith(".mp4"):
                        mp4_file_path = os.path.join(downloaded_content, file)
                        mp3_file_path = os.path.join(
                            downloaded_content, file[:-4] + ".mp3")

                        video = VideoFileClip(mp4_file_path)
                        video.audio.write_audiofile(mp3_file_path)

                        print(
                            f"[~] {mp4_file_path[40:]} converted to {mp3_file_path[40:]}")

                        os.remove(mp4_file_path)
                        print(f"[~] {mp4_file_path[40:]} removed")
            else:
                print("[~] No mp4 files to convert")
        return wrapper
    return decorator

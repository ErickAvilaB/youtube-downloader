""" Converter module """
import os


def convert_mp4_to_mp3(downloaded_content):
    """ Decorator to convert mp4 downloaded files to mp3 """
    def decorator(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)

            mp4_list_files = [
                file for file in os.listdir(downloaded_content) if file.endswith(".mp4")]

            if mp4_list_files:
                print("[+] Let's convert all downloads folder mp4 files to mp3")
                for element in mp4_list_files:
                    mp4_file_path = os.path.join(downloaded_content, element)
                    mp3_file_path = os.path.join(
                        downloaded_content, element[:-4] + ".mp3")

                    os.rename(mp4_file_path, mp3_file_path)

                    print(
                        f"[+] {mp4_file_path[40:]} converted to {mp3_file_path[40:]}")
                    print("[    -----    ]")
            else:
                print("[!] No mp4 files to convert")

            print("[                   ---  (づ｡◕‿‿◕｡)づ  ---                  ]")
        return wrapper
    return decorator

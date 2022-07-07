""" Converter module """
import os


# Take the folder where the videos are stored
def convert_mp4_to_mp3(downloaded_content):
    """ Decorator to convert mp4 downloaded files to mp3 """
    def decorator(function):
        def wrapper(*args, **kwargs):
            # First execute the function gived at the decorator
            function(*args, **kwargs)

            # Create list of mp4 files in the folder
            mp4_list_files = [
                file for file in os.listdir(downloaded_content) if file.endswith(".mp4")]

            # Validate if list is empty
            if mp4_list_files:
                print("[+] Let's convert all downloads folder mp4 files to mp3")
                for element in mp4_list_files:
                    # Generate path for each mp4 file
                    mp4_file_path = os.path.join(downloaded_content, element)
                    mp3_file_path = os.path.join(
                        downloaded_content, element[:-4] + ".mp3")

                    # Convert mp4 to mp3 just changing the extension
                    os.rename(mp4_file_path, mp3_file_path)

                    print(
                        f"[+] {mp4_file_path[40:]} converted to {mp3_file_path[40:]}")
                    # Show bar to separate each element
                    print("[    -----    ]")
            else:
                print("[!] No mp4 files to convert")

            # Show bar to separate the main from the convertion
            print("[                   ---  (づ｡◕‿‿◕｡)づ  ---                  ]")
        return wrapper
    return decorator

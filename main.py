import os
from modules.download_music import download_by_name
from modules.converter import convert_mp4_to_mp3


root = os.getcwd()
path_downloads = os.path.join(root, "downloads")
tracklist_file = os.path.join(root, "tracklist.txt")

try:
    os.mkdir(path_downloads)
except FileExistsError:
    pass


@convert_mp4_to_mp3(path_downloads)
def main(folder_for_downloads):
    while True:
        input_option = input(
            "Download: [a] by name, [b] by tracklist, [q] to quit: ")

        if input_option == "a":
            download_by_name(folder_for_downloads)

        elif input_option == "b":
            pass

        elif input_option == "q":
            print("[~] Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main(path_downloads)

""" Script to download music """
import os
from modules.downloader import download_by_name, download_by_tracklist
from modules.converter import convert_mp4_to_mp3


root = os.getcwd()
path_downloads = os.path.join(root, "downloads")
tracklist_file = os.path.join(root, "list.txt")

try:
    os.mkdir(path_downloads)
    open(tracklist_file, "x")
except FileExistsError:
    pass


@convert_mp4_to_mp3(path_downloads)
def main(folder_for_downloads):
    """ Main function. """
    while True:
        input_option = input(
            "Download: [a] by name, [b] by tracklist, [q] to quit: ")

        if input_option == "a":
            download_by_name(folder_for_downloads)

        elif input_option == "b":
            download_by_tracklist(tracklist_file, path_downloads)

        elif input_option == "q":
            print("[~] Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main(path_downloads)

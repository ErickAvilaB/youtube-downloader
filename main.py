""" Script to download music """

import os
from modules.downloader import download_by_name, download_by_tracklist
from modules.converter import convert_mp4_to_mp3


# getcwd get the current working directory, is used create the full path of necessary files
root = os.getcwd()
path_downloads = os.path.join(root, "downloads")
tracklist_file = os.path.join(root, "list.txt")

# Create directory for downloads and tracklist file
try:
    os.mkdir(path_downloads)
    open(tracklist_file, "x")
except FileExistsError:
    pass


# Function to convert downloaded videos to mp3, is called when main ends.
@convert_mp4_to_mp3(path_downloads)
def main(folder_for_downloads, file):
    """ Main function. """

    # Execute pregram always until user quits
    while True:
        input_option = input(
            "[+] Download: [a] by name, [b] by tracklist, [q] to quit: ")

        # Input handler. Execute a specific function according to input
        if input_option == "a":
            download_by_name(folder_for_downloads)

        elif input_option == "b":
            download_by_tracklist(file, folder_for_downloads)

        # Break the infinite loop if the input is q
        elif input_option == "q":
            print("[+] Exiting...")
            break

        # If input is empty shows message and ask again
        elif not input_option:
            print("[!] Please enter an option.")
            continue

        else:
            print("[-] Invalid option")

    print("[!] ALL FILES WILL BE CONVERTED UNTIL MAIN FINISH")


if __name__ == "__main__":
    main(path_downloads, tracklist_file)

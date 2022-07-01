import os
from modules.download_music import download_by_name
from modules.converter import convert_downloads_to_mp3


downloads_folder = os.path.join(os.getcwd(), "downloads")

try:
    os.mkdir(downloads_folder)

except FileExistsError:
    pass


@convert_downloads_to_mp3(content=downloads_folder)
def main(**kwargs):
    """ Search the video by name or tracklist and take the first_result then download it """
    downloads = kwargs["folderForDownloads"]

    input_option = int(input("Download: [a] by name, [b] by tracklist: "))

    if input_option == "a":
        download_by_name(downloads)

    else:
        print("Not implemented yet")


if __name__ == "__main__":
    main(folderForDownloads=downloads_folder)

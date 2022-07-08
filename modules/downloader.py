""" Downloader module """
import re
from pytube import YouTube, Search


def download(song_name, folder):
    """ Download function, take the song name and the folder where the video will be stored """
    try:
        # Search for the song in youtube
        yt_search = Search(song_name)
        print("[+] Searching...")

        # Get the first result, comes something like this:
        # <pytube.__main__.YouTube object: videoId=6oHdAA3AqnE>.
        # Take the video id through the characters index
        first_result = str(yt_search.results[0])
        id_video = first_result[41:52]
        url_video = f"https://youtu.be/{id_video}"

        # Create instance of the video passing the url
        yt_video = YouTube(url_video)
        print(f"[+] {yt_video.title} found and will be downloaded")

        # Get a stream, 140 stream has only audio in the best quality
        stream = yt_video.streams.get_by_itag(140)
        stream.download(folder)
        print(f"[+] {yt_video.title} Downloaded!")

    # Catch any error
    except Exception as error:
        print(f"[-] Has been an error: {error}")

    # Print a separator
    finally:
        print("""[    -----    ]
              """)


def download_by_url(folder):
    """ Download by url, just take folder where the video will be stored """
    # Infinite loop to keep asking for a url until the user quits
    while True:
        song_input = input(
            "[+] Enter the url with format (youtu.be/) or (youtube.com/watch?v=). (q) to back: ")

        # Validate the url
        validate = re.search("https://youtu.be/", song_input)
        validate_2 = re.search("https://www.youtube.com/watch?", song_input)

        # Validate if user input is empty
        if not song_input:
            print("[!] You must enter a url")

        # Break the infinite loop and return to the main menu
        elif song_input == "q":
            break

        # When url is invalid shows message
        elif (validate is None) and (validate_2 is None):
            print("[!] Invalid url")

        # When url is valid download the video
        # Keep the same download structure as the download()
        elif (validate is not None) or (validate_2 is not None):
            try:
                yt_video = YouTube(song_input)
                print(f"[+] {yt_video.title} found and will be downloaded")

                # Dowload the video
                stream = yt_video.streams.get_by_itag(140)
                stream.download(folder)
                print(f"[+] {yt_video.title} Downloaded!")

            except Exception as error:
                print(f"[-] Has been an error: {error}")

            finally:
                print("""[    -----    ]
                      """)


def download_by_name(folder):
    """ Download song by name, just take folder where the video will be stored.
    Uses the download() function, song_name is taked by user input """
    # Infinite loop to keep asking for a song name until the user quits
    while True:
        song_input = input("[+] Enter the song name. (q) to back: ")

        # Validate if user input is empty
        if not song_input:
            print("[!] You must enter a song name")

        # Break the infinite loop and return to the main menu
        elif song_input == "q":
            break

        # When song name is valid download the video
        else:
            download(song_input, folder)


def download_by_tracklist(path_tracklist_file, folder):
    """ Download by tracklist, just take folder where the video will be stored.
    Uses the download() function, song_name is taked by the lines of the tracklist_file """
    with open(path_tracklist_file, "r", encoding="utf-8") as file:
        tracklist = file.readlines()

    # Validate if the file is empty
    if tracklist:
        for track in tracklist:
            # Run the download function for each song in the tracklist file
            download(track, folder)

    elif not tracklist:
        print("[-] Tracklist is empty")

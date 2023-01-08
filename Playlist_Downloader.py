from pytube import Playlist

# Video downloading counter
i = 0

playlist = Playlist(input("Enter Playlist Link: "))

print("Total videos in playlist: ", len(playlist.video_urls))

# Get permission
ask = input("Do you want to Download it [yes/no]? ")

if (ask == "yes" or ask == "Yes"):
    # Prompt user for resolution
    ask_resolution = int(input(
        "Choose resolution for videos:\n type:\n\t 1 for 144p\n\t 2 for 240p\n\t 3 for 360p\n\t 4 for 480p\n\t 5 for 720p\n"))

    if (ask_resolution == 1):
        resolution = "144p"
    elif (ask_resolution == 2):
        resolution = "240p"
    elif (ask_resolution == 3):
        resolution = "360p"
    elif (ask_resolution == 4):
        resolution = "480p"
    elif (ask_resolution == 5):
        resolution = "720p"
    else:
        print(f"Not a valid value try again!")
        quit

    # Start Downloading
    for video in playlist.videos:
        video.streams.get_by_resolution(resolution).download()
        i += 1
        print(f"Video {i} downloaded")
    print("All Downloaded Successfully ✓\nWith all my respect -OMAR ABSI")
elif (ask == "no" or ask == "No"):
    print("Ok, as you like")
else:
    print("Enter a valid value")

from pytube import YouTube
from sys import argv

link = argv[1]                              # The first line from the cmd will be used as the YouTube website video link
yt = YouTube(link)                          # Which will be stored here

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()    # Retrieves the highest resolution of the video for download

yd.download('C:\Downloads')                 # And stores the video in the computers main download folder, which can be changed to users preference

# If instructions are not in README file.
# Run through terminal with line: python ytDownloader.py "Replace text with YouTube link here"
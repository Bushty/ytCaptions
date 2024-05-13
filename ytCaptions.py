## https://github.com/jdepoix/youtube-transcript-api

from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from sys import argv
import os

# return Downloadpath depending on OS 
def getDownloadPath():
    homePath = os.path.expanduser("~")
    desktopPath = os.path.join(homePath, "Desktop")
    downloadFolderPath = os.path.join(desktopPath, "ytCaptions")
    if not os.path.exists(downloadFolderPath):
        os.makedirs(downloadFolderPath)
        print(f"Folder #{downloadFolderPath} created successfully")
    return downloadFolderPath

# checks if provided link actually links to a YT playlist or video
def validYTLink(link):
    if link.startswith("https://www.youtube.com/") | link.startswith("https://youtu.be/"):
        return True
    return False

# downloads captions
def downloadCaptions(videoLink):
    downloadPath = getDownloadPath()
    videoId = videoLink[len("https://www.youtube.com/watch?v="):]

    video = YouTube(videoLink)
    vTitle = video.title
    vAuthor = video.author
    print("Downloading Captions for Video: ", vTitle, " by ", vAuthor)

    transcript = YouTubeTranscriptApi.get_transcript(videoId)
    formatter = TextFormatter()
    formattedTranscript = formatter.format_transcript(transcript)

    fileName = "Transcript - " + vTitle
    filePath = os.path.join(downloadPath, fileName)
    with open(filePath, 'w', encoding='utf-8') as file:
        file.write(formattedTranscript)
    print("File created: ", filePath)


## Script Start ##
print()
print("This tool can download the captions for Youtube Videos and store them in a text file")
print("Please provide a valid Youtube Link for downloading")

# Repeated User Input prompt till valid Link is entered
inputValid = False
ytLink = ""
while not inputValid:
    user_input = input("Enter Youtube Link: ")
    if user_input == "":
        print()
        print("Exiting Tool")
        print()
        break
    elif validYTLink(user_input):
        ytLink = user_input
        inputValid = True
        break
    else:
        print("Entered Link is not a valid URL.")
        print("Please enter a valid Link or Press Enter to exit")
        print()

# depending if video / playlist calls appropiate download function
if inputValid: 
        downloadCaptions(ytLink)
        print()
        print("Captions Download finished")
        print()
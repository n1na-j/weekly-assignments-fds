import json

playlist = []

# Add new song
def addSong(artist, album, song):
    newSong = {"artist": artist, "album": album, "song": song}
    playlist.append(newSong)

# Count number of songs
def numberOfSongs():
    number = len(playlist)
    return number

# Show playlist
def showPlaylist():
    for show in playlist:
        print(show["song"], "by", show["artist"], "found on", show["album"])

# Play a song
def playSong(songtitle):
    for show in playlist:
        if(songtitle == show["song"]):
            print("Now playing:", show["song"], "by", show["artist"])

# Open de playlist
def openPlaylist():
    with open("songs.json") as json_file:
        data = json.load(json_file)
        return data

# Save a playlist
def savePlaylist():
    with open("songs.json", "w") as outfile:
        json.dump(playlist, outfile)

playlist = openPlaylist()
showPlaylist()
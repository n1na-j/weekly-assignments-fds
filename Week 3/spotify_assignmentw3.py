# Import json
import json

# Import spotify.py
import spotify

# Default login is False
logged_in = False


# The user accounts
accounts = []



# Open the original Spotify playlist
playlist = spotify.openPlaylist()



# Open the json file with user accounts
def open_users():
    with open("accounts.json") as json_file:
        accounts = json.load(json_file)
        return accounts 

user_data = open_users()



#  Login function
def correctLogin():
    # User input
    name_input = input("Username: ")
    password_input = input("Password: ")

    # Check if the username and password are correct
    for user in user_data :
        if name_input == user["loginname"] and password_input == user["password"]:
            global role
            role = user["role"]
            print("Successfully logged in")
            return True
            #Show Spotify playlist
            
    # Return False when log in failed
    print("Incorrect username or password. Please try again.")
    return False
user_loggedin = correctLogin()


# Users with the role "owner" can add a user if the user (owner) is logged in
def addUser(isOwner):

    # Check if the user has the role of an owner when the user is logged in
    if user_loggedin and isOwner == "owner":
        # User can add a new user
        new_username = input("New username: ")
        new_password = input("New password: ")
        # New user created
        new_user = {"loginname": new_username, "password": new_password, "role":"family member"}
        # Add new user to the JSON file
        def save_users(filename):
            with open(filename, "w") as output_file:
                json.dump(accounts, output_file)
        accounts = user_data
        accounts.append(new_user)
        save_users("accounts.json")
        
      

    # Go to this line when the user is not the owner
    elif isOwner != "owner":
        print("You don't have the right permissions to add a new user account")
        return
    
    # Go to this line when the user is not logged in 
    else:
        print("You have to be logged in before you can make any changes")
# Look at the role
addUser(role)

# User can add a song to the Spotify playlist
def newSong():
  
    # The user must be logged in
    if user_loggedin:
        new_artist = input("Artist: ")
        new_album = input("ALbum: ")
        new_title = input("Song: ")

        new_song = {"artist": new_artist, "album": new_album, "song": new_title}
     
        def savePlaylist(filename):
            with open(filename, "w") as outfile:
                json.dump(playlist, outfile)
        new_playlist = playlist
        new_playlist.append(new_song)
        savePlaylist("new_songs.json")
newSong()


# Show the new playlist 
def open_new_Playlist():
    with open("new_songs.json") as json_file:
        data = json.load(json_file)
        return data
show_new_playlist  = open_new_Playlist()
print("This is the new playlist: ", show_new_playlist)



# Show the number of users
def totalUsers():
    return(len(user_data))
total = totalUsers()
print("Total users:", total)


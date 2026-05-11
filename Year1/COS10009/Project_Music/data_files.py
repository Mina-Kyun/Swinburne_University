import input_functions
GENRE = {
    1: "Pop",
    2: "Classic",
    3: "Jazz",
    4: "Rock"
}

class Album():
    def __init__(self, artist_name, album_name, release_date, genre, tracks):
        self.artist_name = artist_name
        self.album_name = album_name
        self.release_date = release_date
        self.genre = genre
        self.tracks = tracks
        
class Track():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
def read_file():
    filename = 'albums.txt'
    try:
        music_file = open(filename, "r")
        count = int(music_file.readline().strip())
    except:
        print("Error files")
        return []
    albums = []
    i = 0
    while i < count:
        album = read_album(music_file)
        albums.append(album)
        i += 1
    music_file.close()
    return albums

def read_album(music_file):
    artist_name = music_file.readline().strip()
    album_name = music_file.readline().strip()
    release_date = music_file.readline().strip()
    genre = GENRE[int(music_file.readline().strip())]
    tracks = read_tracks(music_file)
    print("Reading album:", artist_name, "-", album_name)
    album = Album(artist_name, album_name, release_date, genre, tracks)
    return album

def read_track(music_file):
    name = music_file.readline().strip()
    location = music_file.readline().strip()
    track = Track(name, location)
    return track

def read_tracks(music_file):
    count = int(music_file.readline().strip())
    tracks = []
    i = 0
    while i < count:
        track = read_track(music_file)
        tracks.append(track)
        i += 1
    return tracks

def print_album(album):
    print(f"The artist name: {album.artist_name}")
    print(f"The album name: {album.album_name}")
    print(f"The release date of the album: {album.release_date}")
    print(f"The genre of the album: {album.genre}")
    print_tracks(album.tracks)

def print_albums(albums):
    i = 0
    while i < len(albums):
        print(f"{i+1}. {albums[i].artist_name} - {albums[i].album_name} - {albums[i].release_date} - {albums[i].genre}")
        i += 1
    
def print_track(track):
    print(track.name)
    print(track.location)

def print_tracks(tracks):
    i = 0
    while i < len(tracks):
        print(i+1, tracks[i].name)
        print(tracks[i].location)
        i += 1
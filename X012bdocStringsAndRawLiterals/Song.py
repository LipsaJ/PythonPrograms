class Song:
    """
    Class to represent a song

    Attributes:
        title: The title of the song
        artist(Artist): The creator of the song
        duration(int): duration in seconds, if not specified then 0
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    class to represent album using its track

    Attributes:
        name(str): The name of the album
        year(int): The release year
        artist(Artist): the artist responsible for creation, if not specified then none
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("various artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """
        Adds a song to the track list

        Args:
            song(Song): a song to be added.
            position: If specified the song will be added or will be added to the end
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    def __init__(self, name):
        self.name = name
        self.album = []

    def add_album(self, album):
        self.album.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data rows should consists of artist, album, year, song
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # we have just read details for a new artist
                # store the current album in the artist section and then create a new album as well
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # we have just read a new album for the current artist
                # store the current album in artists section and create a new album
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new son objects and add it to album_collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After reading the last line of text file, we have an artist and album that havent been stored-
        # process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparision with original file"""
    with open("checkfile", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.album:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)

class Song:
    # Class-level attributes to keep track of the counts
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the total song count
        Song.count += 1

        # Track genres and artists
        Song.genres.add(genre)
        Song.artists.add(artist)
        
        # Track count of songs by genre
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
        # Track count of songs by artist
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1



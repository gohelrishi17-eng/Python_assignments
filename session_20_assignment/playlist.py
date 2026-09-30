class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)

    def get_songs(self):
        return self._songs


playlist = Playlist()

playlist.add_song("Kesariya")
playlist.add_song("Apna Bana Le")
playlist.add_song("Tum Se Hi")

print("Songs:", playlist.get_songs())

playlist.remove_song("Apna Bana Le")

print("Updated Songs:", playlist.get_songs())

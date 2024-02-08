class MusicLibrary:

    def __init__(self):
        self._music_library = []

    def add(self, track):
        return self._music_library.append(track)

    def all(self):
        return self._music_library

    def search_by_title(self, keyword):
        return [track for track in self._music_library if keyword.upper() in track.format()]
    
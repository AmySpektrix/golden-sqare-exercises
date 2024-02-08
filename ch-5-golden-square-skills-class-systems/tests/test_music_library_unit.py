from lib.music_library import MusicLibrary
from lib.track import Track

def test_music_library():
    library = MusicLibrary()

"""
When we search an empty list a word not in any track title
We get an empty list back
"""

def test_search_by_bit_not_in_title():
    library = MusicLibrary()
    assert library.search_by_title("zzz") == []

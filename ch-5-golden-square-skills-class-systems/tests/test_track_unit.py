from lib.track import Track

def test_track():
    track_test = Track("Always The Hard Way", "Terror")

"""
Given a new track instantiated with a title and artist
track.title returns the title and track.artist returns the artist
"""
def test_attribute_filling():
    track_test = Track("Always The Hard Way", "Terror")
    assert track_test.title == "Always The Hard Way"
    assert track_test.artist == "Terror"

"""
Given a track with a title and artist
#format returns a string like TITLE by ARTIST
"""
def test_track_format():
    track_test = Track("Always The Hard Way", "Terror")
    assert track_test.format() == "ALWAYS THE HARD WAY by TERROR"
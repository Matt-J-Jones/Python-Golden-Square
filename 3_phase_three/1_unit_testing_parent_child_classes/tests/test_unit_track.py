from lib.track import Track

def test_creates_object():
    track = Track("title", "artist")
    assert isinstance(track, Track)

def test_keyword_search_matches_title():
    track = Track("title", "artist")
    assert track.matches("title") is True

def test_keyword_search_matches_artist():
    track = Track("title", "artist")
    assert track.matches("artist") is True

def test_keyword_search_does_not_matche():
    track = Track("title", "artist")
    assert track.matches("none") is False
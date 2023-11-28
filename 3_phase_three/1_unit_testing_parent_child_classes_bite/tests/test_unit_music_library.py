from lib.music_library import MusicLibrary
from unittest.mock import Mock

def test_creates_object():
    library = MusicLibrary()
    assert isinstance(library, MusicLibrary)

def test_adds_mock_tracks_to_library():
    library = MusicLibrary()
    fake_track_true = Mock()
    fake_track_true.matches.return_value = True
    fake_track_false = Mock()
    fake_track_false.matches.return_value = False

    library.add(fake_track_true)
    library.add(fake_track_true)
    library.add(fake_track_false)

    assert len(library.search("value")) == 2

def test_adds_17_mock_tracks_to_library():
    library = MusicLibrary()
    fake_track_true = Mock()
    fake_track_true.matches.return_value = True
    fake_track_false = Mock()
    fake_track_false.matches.return_value = False

    for x in range(10):
        library.add(fake_track_true)
    for x in range(7):
        library.add(fake_track_false)

    assert len(library.search("value")) == 10
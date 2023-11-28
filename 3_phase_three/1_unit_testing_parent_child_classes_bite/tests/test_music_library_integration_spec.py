from lib.track import Track
from lib.music_library import MusicLibrary

def test_creates_objects():
    library = MusicLibrary()
    track = Track("title", "artist")
    assert isinstance(library, MusicLibrary)
    assert isinstance(track, Track)


def test_adds_tracks_to_library():
    library = MusicLibrary()
    track_1 = Track("Break Stuff", "Limp Bizkit")
    track_2 = Track("My Generation", "Limp Bizkit")
    track_3 = Track("Take a Look Around", "Limp Bizkit")
    track_4 = Track("Tonight, Tonight", "Smashing Pumpkins")
    track_5 = Track("1979", "Smashing Pumpkins")
    
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    library.add(track_4)
    library.add(track_5)
    
    assert len(library.search("Limp Bizkit")) == 3
    assert len(library.search("Smashing Pumpkins")) == 2
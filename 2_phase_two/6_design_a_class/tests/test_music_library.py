from lib.music_library import MusicLibrary
import pytest

def test_creates_object():
    music_library = MusicLibrary()
    assert isinstance(music_library, MusicLibrary)

def test_add_song_print_list():
    music_library = MusicLibrary()
    music_library.add("Echo Chamber Experiment", "Stardust Serenade")
    assert music_library.print_list() == ["Echo Chamber Experiment - Stardust Serenade"]

def test_add_five_songs_prints_list():
    music_library = MusicLibrary()
    music_library.add("Echo Chamber Experiment", "Stardust Serenade")
    music_library.add("Celestial Pulse", "Echoes of Infinity")
    music_library.add("Electric Echoes", "Eclipsed Dreams")
    music_library.add("Crimson Horizon", "Aurora Borealis Blues")
    music_library.add("Crimson Horizon", "Nebula Waltz")
    assert music_library.print_list() == [
     "Echo Chamber Experiment - Stardust Serenade",
     "Celestial Pulse - Echoes of Infinity",
     "Electric Echoes - Eclipsed Dreams",
     "Crimson Horizon - Aurora Borealis Blues",
     "Crimson Horizon - Nebula Waltz"]

def test_add_empty_song_title_raise_error():
    music_library = MusicLibrary()
    with pytest.raises(Exception) as e:
        music_library.add("Echo Chamber Experiment", "")
    error_message = str(e.value)
    assert error_message == "Song Title cannot be empty"

    with pytest.raises(Exception) as e:
        music_library.add("Echo Chamber Experiment", None)
    error_message = str(e.value)
    assert error_message == "Song Title cannot be empty"

def test_add_empty_band_name_raise_error():
    music_library = MusicLibrary()
    with pytest.raises(Exception) as e:
        music_library.add("", "Stardust Serenade")
    error_message = str(e.value)
    assert error_message == "Band Name cannot be empty"

    with pytest.raises(Exception) as e:
        music_library.add(None, "Stardust Serenade")
    error_message = str(e.value)
    assert error_message == "Band Name cannot be empty"

def test_add_empty_name_and_title_raise_error():
    music_library = MusicLibrary()
    with pytest.raises(Exception) as e:
        music_library.add("", "")
    error_message = str(e.value)
    assert error_message == "Song Title & Band Name cannot be empty"

    with pytest.raises(Exception) as e:
        music_library.add(None, None)
    error_message = str(e.value)
    assert error_message == "Song Title & Band Name cannot be empty"
    
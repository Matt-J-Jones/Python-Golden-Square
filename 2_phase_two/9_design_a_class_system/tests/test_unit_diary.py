from lib.diary import Diary

def test_creates_object():
    diary = Diary()
    assert isinstance(diary, Diary)

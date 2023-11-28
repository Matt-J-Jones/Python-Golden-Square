from lib.diary import Diary

def test_creates_object():
    diary = Diary("Text")
    assert isinstance(diary, Diary)
    
def test_returns_entry():
    diary = Diary("Text")
    assert diary.read() == "Text"
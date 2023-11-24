from lib.diary_entry import DiaryEntry

def test_creates_object():
    diary_entry = DiaryEntry("Title", "Hello World")
    assert isinstance(diary_entry, DiaryEntry)
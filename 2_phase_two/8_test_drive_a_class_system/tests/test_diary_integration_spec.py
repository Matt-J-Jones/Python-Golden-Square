from lib.diary import Diary
from lib.diary_entry import DiaryEntry


def test_creates_diary_object():
    diary = Diary()
    diary_entry = DiaryEntry("Title", "Hello World")
    assert isinstance(diary, Diary)
    assert isinstance(diary_entry, DiaryEntry)
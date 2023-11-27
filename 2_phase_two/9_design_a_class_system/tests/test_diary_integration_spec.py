from lib.diary import Diary
from lib.diary_entry import DiaryEntry


def test_creates_diary_object():
    diary = Diary()
    diary_entry = DiaryEntry(["Title", "Hello World"])
    assert isinstance(diary, Diary)
    assert isinstance(diary_entry, DiaryEntry)
    
def test_adds_single_entry_to_diary():
    diary = Diary()
    diary_entry = DiaryEntry(["Title", "Hello World"])
    diary.add(diary_entry)
    assert diary.all() == "Title: Hello World"

def test_adds_entry_to_diary_returns_count():
    diary = Diary()
    diary_entry = DiaryEntry(["Title", "Hello World"])
    diary.add(diary_entry)
    assert diary.count_words() == 2

def test_adds_five_entries_to_diary():
    diary = Diary()
    diary_entry = DiaryEntry(["Title", "Hello World"])
    diary.add(diary_entry)
    diary.add(diary_entry)
    diary.add(diary_entry)
    diary.add(diary_entry)
    diary.add(diary_entry)
    assert diary.count_words() == 10
    assert diary.reading_time(5) == 2
    assert diary.all() == "Title: Hello World\nTitle: Hello World\nTitle: Hello World\nTitle: Hello World\nTitle: Hello World"

def test_adds_multiple_finds_entry_for_reading_time():
    diary = Diary()
    diary_entry_short = DiaryEntry(["Entry 1", "Hello World"])
    diary_entry_middle = DiaryEntry(["Entry 2", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ut."])
    diary_entry_long = DiaryEntry(["Entry 3", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vel nunc nunc. Phasellus volutpat, eros hendrerit suscipit sollicitudin, tortor nisl molestie sapien, quis mattis ex."])
    diary.add(diary_entry_short)
    diary.add(diary_entry_middle)
    diary.add(diary_entry_long)
    assert diary.count_words() == 37
    assert diary.find_best_entry_for_reading_time(1,10) == "Entry 2: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ut."

def test_adds_multiple_reversed_finds_entry_for_reading_time():
    diary = Diary()
    diary_entry_short = DiaryEntry(["Entry 1", "Hello World"])
    diary_entry_middle = DiaryEntry(["Entry 2", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ut."])
    diary_entry_long = DiaryEntry(["Entry 3", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vel nunc nunc. Phasellus volutpat, eros hendrerit suscipit sollicitudin, tortor nisl molestie sapien, quis mattis ex."])
    diary.add(diary_entry_long)
    diary.add(diary_entry_middle)
    diary.add(diary_entry_short)
    assert diary.count_words() == 37
    assert diary.find_best_entry_for_reading_time(1,10) == "Entry 2: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ut."
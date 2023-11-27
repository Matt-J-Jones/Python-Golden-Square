from lib.diary_entry import DiaryEntry

EXAMPLE_ENTRY = ["Title", "Hello world"]
EXAMPLE_FORMATTED_CONTENT = "Title: Hello world"
EXAMPLE_WPM = 200

def test_creates_object():
    diary_entry = DiaryEntry(["Title", "Hello World"])
    assert isinstance(diary_entry, DiaryEntry)

def test_creates_object_returns_formatted():
    diary_entry = DiaryEntry(EXAMPLE_ENTRY)
    assert diary_entry.format() == EXAMPLE_FORMATTED_CONTENT

def test_count_words_in_short_entry():
    diary_entry = DiaryEntry(EXAMPLE_ENTRY)
    assert diary_entry.count_words() == 2

def test_count_words_in_long_entry():
    diary_entry = DiaryEntry([EXAMPLE_ENTRY[0], (EXAMPLE_ENTRY[1] + " ") * 100])
    assert diary_entry.count_words() == 200
    
def test_reading_time_long_entry():
    diary_entry = DiaryEntry([EXAMPLE_ENTRY[0], (EXAMPLE_ENTRY[1] + " ") * 100])
    assert diary_entry.reading_time(EXAMPLE_WPM) == 1.0

def test_reading_time_slow_reading_speed():
    diary_entry = DiaryEntry([EXAMPLE_ENTRY[0], (EXAMPLE_ENTRY[1] + " ") * 100])
    assert diary_entry.reading_time(EXAMPLE_WPM / 2) == 2.0
  
def test_read_first_10_words():
    content_long = (EXAMPLE_ENTRY[1] + " ") * 10
    diary_entry = DiaryEntry([EXAMPLE_ENTRY[0], content_long])
    assert diary_entry.reading_chunk(10, 1) == ((EXAMPLE_ENTRY[1] + " ") * 5).rstrip()

def test_read_first_chunk_then_second():
    content_one = "CHUNK_ONE ipsum dolor sit amet, consectetur adipiscing elit. Sed malesuada."
    content_two = "CHUNK_TWO ipsum dolor sit amet, consectetur adipiscing elit. Nam eu."
    diary_entry = DiaryEntry([EXAMPLE_ENTRY[0], content_one + " " + content_two])
    assert diary_entry.reading_chunk(10, 1) == content_one
    assert diary_entry.reading_chunk(10, 1) == content_two

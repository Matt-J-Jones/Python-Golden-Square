from lib.string_builder import StringBuilder

def test_creates_object():
    string  = StringBuilder()
    assert string.size() == 0
    
def test_creates_object_adds_text():
    string  = StringBuilder()
    string.add("abcd")
    assert string.size() == 4

def test_creates_object_adds_text_twice():
    string  = StringBuilder()
    string.add("abcd")
    assert string.size() == 4
    string.add("efgh")
    assert string.size() == 8
    assert string.output() == "abcdefgh"
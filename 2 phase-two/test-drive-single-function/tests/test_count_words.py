from lib.count_words import count_words

def test_returns_value():
    assert count_words("") is not None
    
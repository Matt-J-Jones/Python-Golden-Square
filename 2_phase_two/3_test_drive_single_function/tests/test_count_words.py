from lib.count_words import count_words

def test_returns_value():
    assert count_words("") is not None

def test_returns_two():
    assert count_words("Hello, world") is 2

def test_returns_six():
    assert count_words("there is a spectre haunting europe") is 6
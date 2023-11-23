from lib.make_snippet import make_snippet

def test_returns_value():
    assert make_snippet("") is not None

def test_return_string_of_2_words():
    assert make_snippet("Hello, World") == "Hello, World"

def test_return_string_of_5_words():
    assert make_snippet("This is five words long") == "This is five words long"
  
def test_return_shortened_string():
    assert make_snippet("there is a spectre haunting europe") == "there is a spectre haunting..."
from lib.greet import *

def test_returns_greeting_to_steven():
    result = greet("Steven")
    assert result == "Hello, Steven!"
    
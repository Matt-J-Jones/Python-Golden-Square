from lib.time_to_read import time_to_read
import pytest

def test_returns_value():
    assert time_to_read("Hello World") is not None

def test_returns_1_with_200():
    string_to_test = "Hello World " * 100
    assert time_to_read(string_to_test) == 1.0

def test_returns_2_with_400():
    string_to_test = "Hello World " * 200
    assert time_to_read(string_to_test) == 2.0

def test_returns_1_5_with_300():
    string_to_test = "Hello World " * 150
    assert time_to_read(string_to_test) == 1.5

def test_returns_0_5_with_100():
    string_to_test = "Hello World " * 50
    assert time_to_read(string_to_test) == 0.5
    
def test_retuns_error_with_none_string():
    string_to_test = None
    with pytest.raises(Exception) as e:
        time_to_read(string_to_test)
    error_message = str(e.value)
    assert error_message == "Cannot estimate time for an empty string."
    
def test_retuns_error_with_empty_string():
    string_to_test = ""
    with pytest.raises(Exception) as e:
        time_to_read(string_to_test)
    error_message = str(e.value)
    assert error_message == "Cannot estimate time for an empty string."
    
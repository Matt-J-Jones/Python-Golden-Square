from lib.todo_check import todo_check
import pytest

def test_returns_value():
    assert todo_check("Hello World") is not None

def test_string_starts_with_todo():
    assert todo_check("#TODO: Buy Milk") is True

def test_string_doesnt_contain_todo():
    assert todo_check("Buy Milk") is False

def test_string_contains_toto():
    assert todo_check("Buy Milk, #TODO") is True

def test_string_todo_missing_hash():
    assert todo_check("Buy Milk, TODO") is False

def test_returns_error_with_empty_string():
    string_to_test = ""
    with pytest.raises(Exception) as e:
        todo_check(string_to_test)
    error_message = str(e.value)
    assert error_message == "Cannot check empty string."

def test_returns_error_with_none_string():
    string_to_test = None
    with pytest.raises(Exception) as e:
        todo_check(string_to_test)
    error_message = str(e.value)
    assert error_message == "Cannot check empty string."

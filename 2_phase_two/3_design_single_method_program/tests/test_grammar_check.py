from lib.grammar_check import grammar_check
import pytest

def test_returns_value():
    assert grammar_check("Hello World") is not None

def test_returns_true_if_both_correct():
    assert grammar_check("Hello World!") is True
    
def test_returns_false_if_capital_correct():
    assert grammar_check("Hello World") is False
    
def test_returns_false_if_punctuation_correct():
    assert grammar_check("hello World!") is False
    
def test_returns_false_if_ending_comma():
    assert grammar_check("hello World,") is False

def test_returns_error_with_empty_string():
    string_to_test = ""
    with pytest.raises(Exception) as e:
        grammar_check(string_to_test)
    error_message = str(e.value)
    assert error_message == "Cannot check grammar for an empty string."

def test_returns_error_with_none_string():
    string_to_test = None
    with pytest.raises(Exception) as e:
        grammar_check(string_to_test)
    error_message = str(e.value)
    assert error_message == "Cannot check grammar for an empty string."
from lib.grammar_stats import GrammarStats
import pytest

def test_creates_valid_object():
    grammar_stats = GrammarStats()
    assert isinstance(grammar_stats, GrammarStats)

def test_checks_for_capital_and_punctuation_return_true():
    text_to_check = "Hello, World!"
    grammar_stats = GrammarStats()
    assert grammar_stats.check(text_to_check) is True

def test_checks_for_punctuation_return_false():
    text_to_check = "Hello, World"
    grammar_stats = GrammarStats()
    assert grammar_stats.check(text_to_check) is False

def test_checks_for_capital_return_false():
    text_to_check = "hello, World!"
    grammar_stats = GrammarStats()
    assert grammar_stats.check(text_to_check) is False

def test_returns_error_with_empty_string():
    text_to_check = ""
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(text_to_check)
    error_message = str(e.value)
    assert error_message == "Cannot check grammar for an empty string."

def test_returns_error_with_none_string():
    text_to_check = None
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(text_to_check)
    error_message = str(e.value)
    assert error_message == "Cannot check grammar for an empty string."

def test_run_tests_return_100_correct():
    text_to_check = "Hello, World!"
    grammar_stats = GrammarStats()
    grammar_stats.check(text_to_check)
    grammar_stats.check(text_to_check)
    assert grammar_stats.percentage_good() == 100

def test_run_tests_return_50_correct():
    text_to_check_true = "Hello, World!"
    text_to_check_false = "Hello, World"
    grammar_stats = GrammarStats()
    grammar_stats.check(text_to_check_true)
    grammar_stats.check(text_to_check_false)
    assert grammar_stats.percentage_good() == 50

def test_run_100_tests_return_27_correct():
    text_to_check_true = "Hello, World!"
    text_to_check_false = "Hello, World"
    grammar_stats = GrammarStats()
    for x in range(73):
        grammar_stats.check(text_to_check_false)
    for x in range(27):
        grammar_stats.check(text_to_check_true)
    assert grammar_stats.percentage_good() == 27

def test_run_15_tests_return_5_correct():
    text_to_check_true = "Hello, World!"
    text_to_check_false = "Hello, World"
    grammar_stats = GrammarStats()
    for x in range(10):
        grammar_stats.check(text_to_check_false)
    for x in range(5):
        grammar_stats.check(text_to_check_true)
    assert grammar_stats.percentage_good() == 33
    
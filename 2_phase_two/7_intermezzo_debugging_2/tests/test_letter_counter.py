from lib.letter_counter import LetterCounter
import pytest

def test_creates_object():
    letter_counter = LetterCounter("Hello World")
    assert isinstance(letter_counter, LetterCounter)

def test_digital_punk_is_i2():
    letter_counter = LetterCounter("Digital Punk")
    assert letter_counter.calculate_most_common() == [2, "i"]

def test_hello_world_is_l3():
    letter_counter = LetterCounter("Hello World")
    assert letter_counter.calculate_most_common() == [3, "l"]

def test_long_string_is_correct():
    letter_counter = LetterCounter("aaaathequcikbrownfoxjumpsoverthelazydog")
    assert letter_counter.calculate_most_common() == [5, "a"]#

def test_string_with_spaces_is_correct():
    letter_counter = LetterCounter("          aa")
    assert letter_counter.calculate_most_common() == [2, "a"]

def test_string_with_special_chars_is_correct():
    letter_counter = LetterCounter("123456666666666666666 bbc")
    assert letter_counter.calculate_most_common() == [2, "b"]

def test_string_with_one_letter_is_correct():
    letter_counter = LetterCounter("a")
    assert letter_counter.calculate_most_common() == [1, "a"]
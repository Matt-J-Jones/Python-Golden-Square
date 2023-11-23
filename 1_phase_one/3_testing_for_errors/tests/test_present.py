from lib.present import Present
import pytest

def test_creates_object():
    present = Present()
    assert present.contents == None
    
def test_unwrap_empty():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrap_object():
    present = Present()
    present.wrap("xbox")
    assert present.unwrap() == "xbox"
    
def test_wrap_object_twice():
    present = Present()
    present.wrap("xbox")
    with pytest.raises(Exception) as e:
        present.wrap("another xbox")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


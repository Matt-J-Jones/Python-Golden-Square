import pytest
from lib.password_checker import PasswordChecker

def test_password_is_length_8():
    password = PasswordChecker()
    assert password.check("password") is True

def test_password_is_length_10():
    password = PasswordChecker()
    assert password.check("password??") is True
    
def test_password_is_length_4():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
      password.check("1234")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

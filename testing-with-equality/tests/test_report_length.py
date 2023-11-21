from lib.report_length import *

def test_returns_zero_for_zero_length_string():
    result = report_length("")
    assert result == "This string was 0 characters long."
    
def test_returns_ten_for_ten_length_string():
    result = report_length("ottffssent")
    assert result == "This string was 10 characters long."
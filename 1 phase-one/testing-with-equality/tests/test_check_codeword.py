from lib.check_codeword import *

def test_checks_codeword_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."
  
def test_checks_codeword_incorrect():
    result = check_codeword("dog")
    assert result == "WRONG!"
    
def test_checks_codeword_close():
    result = check_codeword("hearse")
    assert result == "Close, but nope."
     
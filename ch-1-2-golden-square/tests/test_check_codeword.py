from lib.check_codeword import *

def test_if_codeword_is_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_if_codeword_starts_and_ends_with_correct_letters():
    result = check_codeword ("happy house")
    assert result == "Close, but nope."

def test_if_codeword_starts_with_correct_letters_but_ends_with_wrong():
    result = check_codeword ("happy")
    assert result == "WRONG!"

def test_if_codeword_starts_with_incorrect_letter_but_ends_with_correct():
    result = check_codeword ("mouse")
    assert result == "WRONG!"

def test_if_codeword_is_wrong():
    result = check_codeword("banana")
    assert result == "WRONG!"

def test_if_codeword_is_wrong_case():
    result = check_codeword("HORSE")
    assert result == "WRONG!"

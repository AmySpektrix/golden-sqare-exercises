
from lib.sentence_checker import *
import pytest
"""
given a blank string - it should error - "No sentence provided"
"""

def test_sentence_checker_empty():
    with pytest.raises(Exception) as e:
        return sentence_checker("")
    assert str(e.value) == "No sentence provided!"

"""
Given a sentence with a capital letter at the start and ends with correct punctuation it should let you know both things are correct
"""

# sentence_checker("Hello friends!") => "Capital Letter Checked: Correct, Sentence-End Punctuation Checked: Correct"

def test_sentence_checker_correct():
    assert sentence_checker("Hello, my lovely friend Amy.") == "Capital Letter Checked: Correct, Sentence-End Punctuation Checked: Correct"

"""  
Given a sentence without either a capital letter at the start or the correct punctuation it should let you know both these things are missing
""" 
def test_sentence_checker_both_incorrect():
    assert sentence_checker("hello, my lovely friend Amy,") == "Capital Letter Checked: Incorrect, Sentence-End Punctuation Checked: Incorrect"

"""  
Given a sentence without one of either a capital letter at the start or the correct punctuation it should let you know which of these things are missing
""" 
def test_sentence_checker_cap_incorrect():
    assert sentence_checker("hello, my lovely friend Amy!") == "Capital Letter Checked: Incorrect, Sentence-End Punctuation Checked: Correct"

def test_sentence_checker_cap_incorrect_two():
    assert sentence_checker("hello, my lovely friend Amy?") == "Capital Letter Checked: Incorrect, Sentence-End Punctuation Checked: Correct"


def test_sentence_checker_punc_incorrect():
    assert sentence_checker("Hello, my lovely friend Amy,") == "Capital Letter Checked: Correct, Sentence-End Punctuation Checked: Incorrect"


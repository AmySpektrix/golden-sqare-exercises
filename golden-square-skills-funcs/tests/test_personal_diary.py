from lib.personal_diary import *

"""
check make_snippet returns all of five word string
"""
def test_make_snippet_takes_five_word_string():
    assert make_snippet("Hi my name is Amy") == ("Hi my name is Amy")

"""
check make_snippet returns only first five of eleven word string
"""
def test_make_snippet_takes_longer_than_five_word_string():
    assert make_snippet("'What a curious feeling!' said Alice; `I must be shutting up like a telescope.'") == ("'What a curious feeling!' said...")

"""
check make_snippet returns empty string when empty string input
"""
def test_make_snippet_takes_empty_string():
    assert make_snippet("") == ("")

"""
check count_words returns zero for blank string
"""
def test_count_words_takes_empty_string():
    assert count_words("") == 0

"""
check count_words counts strings with punctuation
"""
def test_count_words_takes_sentence():
    assert count_words("'What a curious feeling!' said Alice; `I must be shutting up like a telescope.'") == 14
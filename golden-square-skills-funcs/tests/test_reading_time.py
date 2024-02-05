from lib.reading_time import *
import pytest

'''
Below gives us various chunks of Alice in Wonderland to work with. The full Alice in Wonderland text is 26,441 words.
'''
def _alice_string():
    all_of_alice = open("tests/alice_chunks/Alice Full.txt", "r")
    string_all_alice = all_of_alice.read()
    all_of_alice.close()
    return string_all_alice

def _alice_200_string():
    all_of_alice = open("tests/alice_chunks/Alice 200.txt", "r")
    string_all_alice = all_of_alice.read()
    all_of_alice.close()
    return string_all_alice

def _alice_100_string():
    all_of_alice = open("tests/alice_chunks/Alice 100.txt", "r")
    string_all_alice = all_of_alice.read()
    all_of_alice.close()
    return string_all_alice

def _alice_500_string():
    all_of_alice = open("tests/alice_chunks/Alice 500.txt", "r")
    string_all_alice = all_of_alice.read()
    all_of_alice.close()
    return string_all_alice

alice_string = _alice_string()
alice_100_words = _alice_100_string()
alice_200_words = _alice_200_string()
alice_500_words = _alice_500_string()

"""
Inputting a blank string should raise an exception
"""
def test_reading_time_empty():
    with pytest.raises(Exception) as e:
        return reading_time("",None)
    assert str(e.value) == "No Text Provided!"

"""
Inputting a 200 word string should return 1 minute
"""
def test_reading_time_200_words():
    assert reading_time(alice_200_words,200) == "approx. 0:01:00"

"""
Inputting a longer string should return more minutes
"""
def test_reading_time_500_words():
    assert reading_time(alice_500_words,200) == "approx. 0:02:30"

"""
Input for less than a minute's worth of text this should give a decimal
"""
def test_reading_time_100_words():
    assert reading_time(alice_100_words,200) == "approx. 0:00:30"

"""
Test for long string which will validate to multiple hours and minutes - this should round to 1 decimal place
"""
def test_reading_time_all():
    assert reading_time(alice_string,200) == "approx. 2:12:12"

from lib.diary_entry import *
import pytest

# here are some variables to work with:
def _alice_string_500():
    all_of_alice = open("tests/Alice 500.txt", "r")
    string_all_alice = all_of_alice.read()
    all_of_alice.close()
    return string_all_alice

test_contents_long = _alice_string_500()
test_contents_short = 'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “and what is the use of a book,” thought Alice “without pictures or conversations?”'
test_title = 'Alice in Wonderland'

"""
when the class initialises it creates some instantiated variables self.title and self.contents
"""

def test_init_diary_entry():
    t_diaryentry = DiaryEntry(test_title, test_contents_short)
    assert f"{t_diaryentry.title}, {t_diaryentry.contents}" == f"{test_title}, {test_contents_short}"

"""
if either title or contents are blank it will return an error indicating that a diary entry requires a title and contents
"""
def test_error_blanks_title():
    with pytest.raises(Exception) as e:
        t_diaryentry = DiaryEntry("", test_contents_short)
    assert str(e.value) == "A diary entry needs both a title and contents, one or both are missing!"

def test_error_blanks_contents():
    with pytest.raises(Exception) as e:
        t_diaryentry = DiaryEntry(test_title, "")
    assert str(e.value) == "A diary entry needs both a title and contents, one or both are missing!"

"""
when you format the diary entry of over 5 words it returns a formatted entry "Title : Contents (first 5 words then...)"
"""

def test_formatted_contents_long():
    t_diaryentry = DiaryEntry(test_title, test_contents_short)
    assert t_diaryentry.format() == "Alice in Wonderland: Alice was beginning to get..."

"""
when you format the diary entry of under 5 words it returns a formatted entry "Title : Contents without an ellipsis"
"""

def test_formatted_contents_short():
    t_diaryentry = DiaryEntry(test_title, "Alice was happy.")
    assert t_diaryentry.format() == "Alice in Wonderland: Alice was happy."

"""
when you use the count_words function it will return the number of words in a diary entry
"""

def test_count_words_57_words():
    t_diaryentry = DiaryEntry(test_title, test_contents_short)
    assert t_diaryentry.count_words() == 57

"""
when you use input a number of words per minute a person can read the reading_time function will calculate how long to read the entry in minutes
"""
def test_reading_time_500_words_200_wpm():
    t_diaryentry = DiaryEntry(test_title, test_contents_long)
    assert t_diaryentry.reading_time(200) == "This will take approximately 0:02:30 to read"

"""
when you use reading_chunk for the first time it should return a chunk of contents equal to the length of time required to read at the provided reading speed
"""
def test_reading_chunk_equal_to_length_time():
    t_diaryentry = DiaryEntry(test_title, test_contents_long)
    assert t_diaryentry.reading_chunk(20,1) == "CHAPTER I. Down the Rabbit-Hole Alice was beginning to get very tired of sitting by her sister on the bank,"

"""
when you use reading_chunk for a second time it should return the next chunk of contents starting from the following word, equal to the length of time available to read.
"""
def test_reading_chunk_returns_next_chunk():
    t_diaryentry = DiaryEntry(test_title, test_contents_long)
    t_diaryentry.reading_chunk(62,1)
    assert t_diaryentry.reading_chunk(55,1) == 'So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.'

"""
when you get to the end of the text, the text should end at the end of the text
"""
def test_ending_at_end():
    t_diaryentry = DiaryEntry(test_title, test_contents_long)
    t_diaryentry.reading_chunk(200,2.3)
    assert t_diaryentry.reading_chunk(200,1) == "thought Alice to herself, `after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top"

"""
when you get to the end of the text the next reading chunk should start at the beginning
"""
def test_starting_from_beginning():
    t_diaryentry = DiaryEntry(test_title, test_contents_long)
    t_diaryentry.reading_chunk(200,3)
    assert t_diaryentry.reading_chunk(20,1) == "CHAPTER I. Down the Rabbit-Hole Alice was beginning to get very tired of sitting by her sister on the bank,"

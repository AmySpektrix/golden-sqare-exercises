from lib.diary_entry import *

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
when you format the diary entry of over 5 words it returns a formatted entry "Title : Contents (first 5 words then...)"
"""

def test_formatted_contents_long():
    t_diaryentry = DiaryEntry(test_title, test_contents_short)
    assert t_diaryentry.format() == "Alice in Wonderland: Alice was beginning to get..."

"""
when you format the diary entry of under 5 words it returns a formatted entry "Title : Contents without an elipsis"
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

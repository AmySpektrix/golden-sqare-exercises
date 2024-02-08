Integration Tests

Functions to test in Main Class:
- add => input: an instance of diary entry - return: nothing but adds instance to list of diary entries
- all => return: a list of instances of Diary Entry
```
<!-- example test -->
def test_add_multiple_and_return_all():
    test_diary = Diary()
    test_entry_1 = DiaryEntry

```

- count_words => return: an integer totalling the number of words in all the diary entries
- reading_time => input: wpm - return: an integer representing the reading time in minutes for WHOLE diary
- find_best_entry_for_reading_time => input: wpm & minutes - return: a DiaryEntry instance which is closest to the time BUT not over the time available eg if there is one that will take 2 mins one 5 mins and one 8 minutes, and you have 7 minutes available we want the 5 minute one even though closer to the 8 minute one.

Unit Tests:

Functions just for unit diary entry
- property - title:
- property - contents:
    - TEST - instatiate diary entry with two values can return the values if you call the attributes

- count_words => return: an integer totalling the number of words in a specific entry
    - TEST - diary entry with 10 words returns 10

- reading_time => input: wpm - return: an integer representing the reading time in minutes for WHOLE diary
    - TEST - diary entry with 20 words and a wpm of 10 wpm returns 2
    - TEST - diary entry with 16 words and a wpm of 10 wpm returns 2
    - TEST - diary entry with 13 words and a wpm of 10 wpm returns 1

- reading_chunk => input: wpm, minutes - return: a chunk of text - A string representing a chunk of the contents that the user could read in the given number of minutes. Calling it a second time should return the next chunk until the chunks have finished, at which point start at the beginning again. \
    - TEST - diary entry with 25 words and a wpm of 10 and 2 minutes to read - returns the first 20 words.
    - TEST - diary entry with 25 words and a wpm of 10 and 2 minutes to read - if called twice returns the last 5 words.
    - TEST - diary entry with 25 words and a wpm of 10 and 2 minutes to read - if called three times returns first 20 words.

Diary Unit Test:

- TEST - checking empty diary instantiates and creates => blank list
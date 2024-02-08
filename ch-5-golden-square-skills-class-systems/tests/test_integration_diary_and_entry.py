from lib.diary_entry import DiaryEntry
from lib.diary import Diary

def test_add_multiple_and_return_all():
    test_diary = Diary()
    test_entry_1 = DiaryEntry("8 Feb 2024", "Today I had a lovely day I learned about classes!")
    test_entry_2 = DiaryEntry("9 Feb 2024", "Tomorrow is another day learning about multiple classes!")
    test_diary.add(test_entry_1)
    test_diary.add(test_entry_2)
    assert test_diary.all() == [test_entry_1,test_entry_2]

def test_count_multiple_entries_words():
    test_diary = Diary()
    test_entry_1 = DiaryEntry("8 Feb 2024", "Today I had a lovely day I learned about classes!")
    test_entry_2 = DiaryEntry("9 Feb 2024", "Tomorrow is another day learning about multiple classes!")
    test_diary.add(test_entry_1)
    test_diary.add(test_entry_2)
    assert test_diary.count_words() == 18

def test_reading_time_multiple_entries():
    test_diary = Diary()
    test_entry_1 = DiaryEntry("8 Feb 2024", "Today I had a lovely day I learned about classes!")
    test_entry_2 = DiaryEntry("9 Feb 2024", "Tomorrow is another day learning about multiple classes!")
    test_diary.add(test_entry_1)
    test_diary.add(test_entry_2)
    assert test_diary.reading_time(10) == 2

def test_find_best_entry_for_reading_time():
    test_diary = Diary()
    test_entry_10 = DiaryEntry("10 words", "Today I had a lovely day I learned about classes!")
    test_entry_8= DiaryEntry("8 words", "Tomorrow is another day learning about multiple classes!")
    test_entry_17 = DiaryEntry("17 words", "Today I had a super dooper lovely day and I learned lots and lots about about classes!")
    test_diary.add(test_entry_10)
    test_diary.add(test_entry_8)
    test_diary.add(test_entry_17)
    assert test_diary.find_best_entry_for_reading_time(12,1) == test_entry_10

def test_find_best_entry_for_reading_time_no_eligible_entries():
    test_diary = Diary()
    test_entry_10 = DiaryEntry("10 words", "Today I had a lovely day I learned about classes!")
    test_entry_8= DiaryEntry("8 words", "Tomorrow is another day learning about multiple classes!")
    test_entry_17 = DiaryEntry("17 words", "Today I had a super dooper lovely day and I learned lots and lots about about classes!")
    test_diary.add(test_entry_10)
    test_diary.add(test_entry_8)
    test_diary.add(test_entry_17)
    assert test_diary.find_best_entry_for_reading_time(5,1) == None
from lib.diary import Diary

def test_instantiate_diary_returns_blank_list():
    test_diary = Diary()
    assert test_diary.all() == []

def test_word_count_starts_zero():
    test_diary = Diary()
    assert test_diary.count_words() == 0    

def test_reading_time_starts_zero():
    test_diary = Diary()
    assert test_diary.reading_time(1) == 0    

def test_best_entry_returns_none_when_blank():
    test_diary = Diary()
    assert test_diary.find_best_entry_for_reading_time(1,1) == None     
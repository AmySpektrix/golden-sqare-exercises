from lib.diary_entry import DiaryEntry

def test_instantiate_diary_entry_with_properties():
    test_diary_entry= DiaryEntry("8 Feb 2024", "Today I had a lovely day I learned about classes!")
    assert test_diary_entry.title == "8 Feb 2024"
    assert test_diary_entry.contents == "Today I had a lovely day I learned about classes!"

def test_count_words():
    test_diary_entry= DiaryEntry("8 Feb 2024", "Today I had a lovely day I learned about classes!")
    actual = test_diary_entry.count_words()
    expected = 10
    assert actual == expected

def test_reading_time_entry_no_rounding():
    test_diary_entry= DiaryEntry("8 Feb 2024", "Today I had a lovely day I learned about classes!")
    actual = test_diary_entry.reading_time(10)
    expected = 1        
    assert actual == expected

def test_reading_time_entry_rounding_down():
    test_diary_entry= DiaryEntry("8 Feb 2024", "Today I had a lovely day I learned lots and lots about about classes!")
    actual = test_diary_entry.reading_time(10)
    expected = 1        
    assert actual == expected

def test_reading_time_entry_rounding_up():
    test_diary_entry= DiaryEntry("8 Feb 2024", "Today I had a super dooper lovely day and I learned lots and lots about about classes!")
    actual = test_diary_entry.reading_time(10)
    expected = 2        
    assert actual == expected

def test_reading_chunk_first_chunk():
    test_diary_entry= DiaryEntry("17 words", "Today I had a super dooper lovely day and I learned lots and lots about about classes!")
    actual = test_diary_entry.reading_chunk(10,1)
    expected = "Today I had a super dooper lovely day and I"        
    assert actual == expected

def test_reading_chunk_second_chunk():
    test_diary_entry= DiaryEntry("17 words", "Today I had a super dooper lovely day and I learned lots and lots about about classes!")
    test_diary_entry.reading_chunk(10,1)
    actual = test_diary_entry.reading_chunk(10,1)
    expected = "learned lots and lots about about classes!"        
    assert actual == expected

def test_reading_chunk_third_reset_chunk():
    test_diary_entry= DiaryEntry("17 words", "Today I had a super dooper lovely day and I learned lots and lots about about classes!")
    test_diary_entry.reading_chunk(10,1)
    test_diary_entry.reading_chunk(15,1)
    actual = test_diary_entry.reading_chunk(5,3)
    expected = "Today I had a super dooper lovely day and I learned lots and lots about"        
    assert actual == expected
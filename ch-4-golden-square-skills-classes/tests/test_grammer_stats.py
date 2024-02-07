from lib.grammer_stats import *

"""
If a sentence begins with a capital letter AND ends with a sentence ending punctuation mark - return True, otherwise return false
"""
def test_check_for_true():
    grammar_stats_test = GrammarStats()
    actual = grammar_stats_test.check("Hi my name is Amy!")
    expected = True
    assert actual == expected

"""
If a sentence does not start with a capital and but ends with a punctuation mark OR starts with a capital and does not end with a punctuation mark - return False
"""
def test_check_no_capital_false():
    grammar_stats_test = GrammarStats()
    actual = grammar_stats_test.check("hi my name is Amy!")
    expected = False
    assert actual == expected

def test_check_no_punctuation_false():
    grammar_stats_test = GrammarStats()
    actual = grammar_stats_test.check("Hi my name is Amy,")
    expected = False
    assert actual == expected

def test_check_both_false():
    grammar_stats_test = GrammarStats()
    actual = grammar_stats_test.check("hi my name is Amy,")
    expected = False
    assert actual == expected

"""
If you check to see the "percentage good" with one true statement it will tell you 100 percent of the texts have been checked and are True
"""
def test_check_all_true_100():
    grammar_stats_test = GrammarStats()
    grammar_stats_test.check("Hi my name is Amy!")
    actual = grammar_stats_test.percentage_good()
    expected = 100
    assert actual == expected

"""
If you check to see the percentage good with one true and one false statement it will tell you 50% of the texts were checked and are True
"""
def test_check_third_true_33():
    grammar_stats_test = GrammarStats()
    grammar_stats_test.check("Hi my name is Amy!")
    grammar_stats_test.check("why hello my name is frank")
    grammar_stats_test.check("why hello my name is also frank")   
    actual = grammar_stats_test.percentage_good()
    expected = 33
    assert actual == expected
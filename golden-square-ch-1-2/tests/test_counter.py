from lib.counter import *

#start by checking that blank counter reports a count of zero

def test_empty_counter():
    test_count = Counter()
    assert test_count.report() == "Counted to 0 so far."


# Test adding single postive number to counter - number should be reflected in final report
def test_counter_add_five():
    test_count = Counter()
    test_count.add(5)
    result = test_count.report()

    assert result == "Counted to 5 so far."

# Test adding two positive numbers to counter - sum of numbers should be reflected in final reoport
def test_counter_add_five_then_10():
    test_count = Counter()
    test_count.add(5)
    test_count.add(10)    
    result = test_count.report()

    assert result == "Counted to 15 so far."

# Test adding single negative number to counter - number should be reflected in final report
def test_counter_add_five():
    test_count = Counter()
    test_count.add(-5)
    result = test_count.report()

    assert result == "Counted to -5 so far."

# Test adding a positive and then a negative number - sum of numbers should be reflected in final report
def test_counter_add_five_then_minus_10():
    test_count = Counter()
    test_count.add(5)
    test_count.add(-10)    
    result = test_count.report()

    assert result == "Counted to -5 so far."

# Test adding a zero - nothing should be added to final report
def test_counter_add_zero():
    test_count = Counter()
    test_count.add(0)   
    result = test_count.report()

    assert result == "Counted to 0 so far."

# Test adding a float - float should be reflected in final report
def test_counter_add_float():
    test_count = Counter()
    test_count.add(0.5667)   
    result = test_count.report()

    assert result == "Counted to 0.5667 so far."
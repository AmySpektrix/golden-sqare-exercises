from lib.string_builder import *

#Initialisaton - test blank string is blank to start
def test_blank_string():
    blank_string = StringBuilder()
    assert blank_string.output() == ""

# Add two short strings - test output is reflected - the strings add/concatenated together
def test_two_short_strings_output():
    two_strings = StringBuilder()
    two_strings.add("Hi")
    two_strings.add(" ")
    two_strings.add("Amy!")
    assert two_strings.output() == "Hi Amy!"

# Add two short strings - test length is reflected
def test_two_short_strings_length():
    two_strings = StringBuilder()
    two_strings.add("Hi")
    two_strings.add(" Amy!")
    assert two_strings.size() == 7

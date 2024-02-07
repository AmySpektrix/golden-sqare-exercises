# GRAMMER CHECK Function Design Recipe

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

suitable sentence-ending punctuation marks = "." "!" or "?" 
Only doing one sentence at a time

What should it output - messages?
 - Capital Letter Checked: Correct, Sentence-End Punctuation Checked: Correct
 - Capital Letter Checked: Every sentence should start with a capital letter, Sentence-End Punctuation Checked: Correct
 - Capital Letter Checked: Correct, Sentence-End Punctuation Checked: Sentences should end with "." "!" or "?"
 - Capital Letter Checked: Every sentence should start with a capital letter, Sentence-End Punctuation Checked: Sentences should end with "." "!" or "?"

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def sentence_checker(sentence):
    "Parameter : Sentence"
        "sentence = a single sentence - string"
    if sentence starts with capital letter and ends with correct punctuation
        "Capital Letter Checked: Correct, Sentence-End Punctuation Checked: Correct"
    if sentence doesnt start with captial letter or ends with punctuation
      "Capital Letter Checked: Every sentence should start with a capital letter, Sentence-End Punctuation Checked: Sentences should end with "." "!" or "?""
    if sentence doesnt start with capital letter but does end with the correct punctuation 
         "Capital Letter Checked: Every sentence should start with a capital letter, Sentence-End Punctuation Checked: Correct"
    if sentence does start with a capital letter but doestnt end correctly
        Capital Letter Checked: Correct, Sentence-End Punctuation Checked: Sentences should end with "." "!" or "?"
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
given a blank string - it should error - "No sentence provided"
"""
sentence_checker("") => "Error: Sentence not Provided"

"""
Given a sentence with a capital letter at the start and ends with correct punctuation it should let you know both things are correct
"""

sentence_checker("Hello friends!") => "Capital Letter Checked: Correct, Sentence-End Punctuation Checked: Correct"

"""  
Given a sentence without either a capital letter at the start or the correct punctuation it should let you know both these things are missing
""" 

sentence_checker("hello friends") => "Capital Letter Checked: Every sentence should start with a capital letter, Sentence-End Punctuation Checked: Sentences should end with "." "!" or "?""

"""  
Given a sentence without one of either a capital letter at the start or the correct punctuation it should let you know which of these things are missing
""" 

sentence_checker("hello friends!") => "Capital Letter Checked: Every sentence should start with a capital letter, Sentence-End Punctuation Checked: Correct"

sentence_checjer("Hello friends") => "Capital Letter Checked: Correct, Sentence-End Punctuation Checked: Sentences should end with "." "!" or "?""



## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

assumptions - 
- we want to see it as a string X number of minutes
- we want round it to 1 decimal place if a float
- we want to error if blank string provided

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def reading_time(text):
    """generates reading time of a text at a speed 200 words per minute

    Parameters: (list all parameters and their types)
       text: the text which the user wants to output the estimated reading time of

    Returns: (state the return value and its type)
        a number of seconds, minutes or hours depending on how long something will take

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
tests/test_reading_time.py
"""
Given an empty string it will error
"""
reading_time("") => "No Text Provided!"

"""
Given a 200 word string it will show one minute
"""
reading_time("<THIS IS A 200 WORD STRING>") => "1.0 minute(s)"

"""
Given a 500 word string it will show two minutes and a half minutes
"""
reading_time("<THIS IS A 500 WORD STRING>") => "2.5 minute(s)"

"""
Given a 100 word string it will show 30 seconds
"""
reading_time("<THIS IS A 100 WORD STRING>") => "0.5 minute(s)"

"""
Given a very long string it will show a big number and round to one decimal place
"""
reading_time("<THIS IS A 25000 WORD STRING>") => "132.2 minute(s)"
"""


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```

Ensure all test function names are unique, otherwise pytest will ignore them!
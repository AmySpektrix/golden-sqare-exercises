from lib.greet import *

def test_greet_with_amy():
    result = greet("Amy")
    assert result == "Hello, Amy!"
import pytest
from lib.password_checker import PasswordChecker

"""
If password is over 8 characters should return True
"""
def test_password_over_eight_char():
    test_checker = PasswordChecker()
    assert test_checker.check("password") == True

"""
If password is under 8 characters should return Error
"""

def test_password_under_eight_char():
    test_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        test_checker.check("pass") == True
    assert str(e.value) == "Invalid password, must be 8+ characters."
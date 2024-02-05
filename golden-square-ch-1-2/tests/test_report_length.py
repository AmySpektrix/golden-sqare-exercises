from lib.report_length import *

def test_short_string():
    result = report_length("hi")
    assert result == "This string was 2 characters long."

def test_medium_string():
    result = report_length("ORANGE MARMALADE")
    assert result == "This string was 16 characters long."

def test_long_string():
    result = report_length('"Well!” thought Alice to herself, “after such a fall as this, I shall think nothing of tumbling down stairs! How brave they’ll all think me at home! Why, I wouldn’t say anything about it, even if I fell off the top of the house!” (Which was very likely true.)')
    assert result == "This string was 259 characters long."

def test_very_long_string_with_line_breaks():
    result = report_length('“Curiouser and curiouser!” cried Alice (she was so much surprised, that for the moment she quite forgot how to speak good English); “now I’m opening out like the largest telescope that ever was! Good-bye, feet!” (for when she looked down at her feet, they seemed to be almost out of sight, they were getting so far off). “Oh, my poor little feet, I wonder who will put on your shoes and stockings for you now, dears? I’m sure I shan’t be able! I shall be a great deal too far off to trouble myself about you: you must manage the best way you can;—but I must be kind to them,” thought Alice, “or perhaps they won’t walk the way I want to go! Let me see: I’ll give them a new pair of boots every Christmas.”/n And she went on planning to herself how she would manage it. “They must go by the carrier,” she thought; “and how funny it’ll seem, sending presents to one’s own feet! And how odd the directions will look!')
    assert result == "This string was 913 characters long."

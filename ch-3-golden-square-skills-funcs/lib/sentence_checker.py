def _capital_letter_check(sentence):
    if sentence[0].isupper():
        return "Capital Letter Checked: Correct"
    else:
        return "Capital Letter Checked: Incorrect"

def _ending_punctuation_check(sentence):
    if sentence[-1] in ".!?":
        return "Sentence-End Punctuation Checked: Correct"
    else:
        return "Sentence-End Punctuation Checked: Incorrect"

def sentence_checker(sentence):
        if sentence == "":
            raise Exception("No sentence provided!")
        else:
            return f"{_capital_letter_check(sentence)}, {_ending_punctuation_check(sentence)}"
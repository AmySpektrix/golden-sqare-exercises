class GrammarStats:
    def __init__(self):
        self.check_true = 0
        self.check_false = 0

    def check(self, text):
        if (text[-1] in ".!?") and (text[0].isupper()):
            self.check_true += 1
            return True
        else:
            self.check_false += 1
            return False

    def percentage_good(self):
        total_checked = (self.check_false+self.check_true)
        return int((self.check_true /total_checked)*100)
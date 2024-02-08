class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        # starts a counter dictionary
        most_common = None
        # starts a variable of the "most common" as none
        most_common_count = 0
        # starts with a count of most common with it starting at 1
        for char in self.text:
        # for each character in the text
            if not char.isalpha():
            # if its NOT a alphabetical character
                continue 
            counter[char] = counter.get(char, 0) +1
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char]
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]
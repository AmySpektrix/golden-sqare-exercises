def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char.isalpha() == True:
            counter[char] = counter.get(char, 0) + 1
            # print(f"number of counts with {char} as the key {counter.get(char, 0)}")
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    # print (sorted(counter.items(), key=lambda item: item[1]))
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
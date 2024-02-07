def make_snippet(string):
    split_string = string.split()
    if len(split_string) >5:
        first_five = split_string[0:5]
        return f"{' '.join(first_five)}..."
    else:
        return string

def count_words(string):
    return len(string.split())
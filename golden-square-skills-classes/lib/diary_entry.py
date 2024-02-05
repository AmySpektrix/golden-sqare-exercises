import datetime
class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("A diary entry needs both a title and contents, one or both are missing!")        #   contents: string
        self.title = title
        self.contents = contents
        self.split_string = self.contents.split()
        self.string_length = len(self.split_string)
        self.reading_chunk_counter = 0

    def format(self):
        if self.string_length >5:
            first_five = self.split_string[0:5]
            return f"{self.title}: {' '.join(first_five)}..."
        else:
            return f"{self.title}: {self.contents}"

    def count_words(self):
        return self.string_length
    
    def reading_time(self, wpm):
        formatted_time= datetime.timedelta(minutes = round((self.string_length/wpm),1))
        return f"This will take approximately {formatted_time} to read"

    def reading_chunk(self, wpm, minutes):
        if self.reading_chunk_counter > self.string_length:
            self.reading_chunk_counter = 0
        chunk_start = self.reading_chunk_counter
        chunk_end = self.reading_chunk_counter + int(round((wpm * minutes),0))
        self.reading_chunk_counter = chunk_end
        return ' '.join(self.split_string[chunk_start:chunk_end])       

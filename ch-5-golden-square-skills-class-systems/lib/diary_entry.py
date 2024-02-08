class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self._string_split= self.contents.split()
        self._string_length = len(self._string_split)
        self._reading_chunk_counter = 0
        
    def count_words(self):
        return self._string_length 

    def reading_time(self, wpm):
        return int(round((self._string_length/wpm),0))

    def reading_chunk(self, wpm, minutes):
        if self._reading_chunk_counter >= self._string_length:
            self._reading_chunk_counter = 0
        chunk_start = self._reading_chunk_counter
        chunk_end = self._reading_chunk_counter + int(round((wpm * minutes),0))
        self._reading_chunk_counter = chunk_end
        return ' '.join(self._string_split[chunk_start:chunk_end])
        
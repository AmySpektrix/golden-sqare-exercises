import datetime
class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        if title == "" or contents == "":
            raise Exception("A diary entry needs both a title and contents, one or both are missing!")        #   contents: string
        self.title = title
        self.contents = contents
        self.split_string = self.contents.split()
        self.reading_chunk_counter = 0
        print(self.reading_chunk_counter)

        

    def format(self):
        if len(self.split_string) >5:
            first_five = self.split_string[0:5]
            return f"{self.title}: {' '.join(first_five)}..."
        else:
            return f"{self.title}: {self.contents}"


    def count_words(self):
        return len(self.split_string)


    def reading_time(self, wpm):
        number_of_minutes = self.count_words()/wpm
        time_format= datetime.timedelta(minutes = round(number_of_minutes,1))
        return f"approx. {time_format}"

    def reading_chunk(self, wpm, minutes):
        number_of_words = wpm * minutes
        self.reading_chunk_counter = self.reading_chunk_counter + number_of_words
        print (self.reading_chunk_counter)
        return ' '.join(self.split_string[57:self.reading_chunk_counter])       



        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        

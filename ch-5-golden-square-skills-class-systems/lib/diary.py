
class Diary:
    def __init__(self):
        self._diary_container = []

    def add(self, entry):
        return self._diary_container.append(entry)

    def all(self):
        return self._diary_container

    def count_words(self):
        return sum([entry.count_words() for entry in self._diary_container])

    def reading_time(self, wpm):
        return int(round(self.count_words()/wpm,0))

    def find_best_entry_for_reading_time(self, wpm, minutes):
        entry_word_max = wpm * minutes
        eligible_entries = [entry for entry in self._diary_container if entry.count_words()<=entry_word_max]
        if eligible_entries == []:
            return None
        return max(eligible_entries, key= lambda entry: entry.count_words())


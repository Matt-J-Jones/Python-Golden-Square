class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        all_entries = []
        for item in self.entries:
            all_entries.append(item.format())
        return "\n".join(all_entries)

    def count_words(self):
        total = 0
        for item in self.entries:
            total += item.count_words()
        return total

    def reading_time(self, wpm):
        total = 0
        for item in self.entries:
            total += item.reading_time(wpm)
        return total

    def find_best_entry_for_reading_time(self, wpm, minutes):
        length_to_find = minutes * wpm
        entries_to_return = []

        for item in self.entries:
            if item.reading_time(wpm) <= length_to_find:
                entries_to_return.append(item.format())

        return max(entries_to_return, key=len)

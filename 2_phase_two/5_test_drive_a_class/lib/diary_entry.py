class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.current_chunk_flag = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return self.count_words() / wpm

    def reading_chunk(self, wpm, minutes):
        start = self.current_chunk_flag
        end = start + (wpm * minutes)
        split_contents = self.contents.split()
        current_chunk = " ".join(split_contents[start:end])
        self.current_chunk_flag = end
        return current_chunk
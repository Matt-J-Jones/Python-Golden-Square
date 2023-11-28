class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        if keyword == self.title or keyword == self.artist:
            return True
        return False
  
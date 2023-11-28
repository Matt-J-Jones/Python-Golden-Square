class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def search(self, keyword):
        return_list = []
        for track in self.tracks:
            if track.matches(keyword) is True:
                return_list.append(track)
        return return_list

class MusicLibrary:
    def __init__(self):
        self.track_list = []

    def add(self, band_name, track_name):
        if track_name == "" == band_name or (track_name is None and band_name is None):
            raise Exception("Song Title & Band Name cannot be empty")
        elif track_name == "" or track_name is None:
            raise Exception("Song Title cannot be empty")
        elif band_name == "" or band_name is None:
            raise Exception("Band Name cannot be empty")
        self.track_list.append(band_name + " - " + track_name)

    def print_list(self):
        return self.track_list
  
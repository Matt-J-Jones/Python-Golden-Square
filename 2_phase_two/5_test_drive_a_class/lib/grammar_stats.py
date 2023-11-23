class GrammarStats:
    def __init__(self):
        self.total_checked = 0
        self.percent_correct = 0
  
    def check(self, text):
        self.total_checked += 1
        if text == None or text == "":
            raise Exception("Cannot check grammar for an empty string.")

        if text[-1] in "!.?":
            if text[0].isupper():
                self.percent_correct += 1
                return True
        return False

    def percentage_good(self):
        return int((self.percent_correct / self.total_checked) * 100)
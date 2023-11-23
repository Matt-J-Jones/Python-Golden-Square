def time_to_read(text):
    if text is None or text == "":
        raise Exception("Cannot estimate time for an empty string.")
    reading_speed = 200
    word_count = len(text.split())
    return word_count/reading_speed
  
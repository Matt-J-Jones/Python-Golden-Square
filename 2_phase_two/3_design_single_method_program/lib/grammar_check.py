def grammar_check(string):
    if string == None or string == "":
        raise Exception("Cannot check grammar for an empty string.")

    if string[-1] in "!.?":
        if string[0].isupper():
            return True
    return False

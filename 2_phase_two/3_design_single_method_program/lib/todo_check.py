def todo_check(string):
    if string is None or string == "":
        raise Exception("Cannot check empty string.")
    if "#TODO" in string:
        return True
    return False
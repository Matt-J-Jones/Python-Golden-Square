def make_snippet(str):
    str_split = str.split()
    if len(str_split) <= 5:
        return str
    elif len(str_split) > 5:
        return " ".join(str_split[0:5]) + "..."
    return None
  
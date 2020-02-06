def is_isogram(string):
    return len(list(string.lower())) == len(set(string.lower()))
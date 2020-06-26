import string

def remove_punctuation(inStr):
    return inStr.translate(string.maketrans('', ''), string.punctuation)

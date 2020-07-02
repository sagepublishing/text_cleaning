import string
translator=str.maketrans('','',string.punctuation)

def remove_punctuation(inStr):
    return inStr.translate(translator)

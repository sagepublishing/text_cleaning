"""This module contains method to lemmatize sentence using textblob"""
# source: https://textblob.readthedocs.io/en/dev/quickstart.html

from textblob import Word


def lemmatize_sentence_textblob(string_value):
    """
    lemmatize sentence using textblob
    :param string_par: source string
    :return: filtered string
    """
    words = string_value.split(" ")
    tokens = []
    for word in words:
        word_val = Word(word)
        tokens.append(word_val.lemmatize())
    return " ".join(tokens)

"""This module contains method to filter out stopwords with the
exception of custom stopwords list"""

from gensim import utils
from gensim.parsing.preprocessing import STOPWORDS


def remove_stopwords_except(string_value: str, opts: dict):
    """Filters out stopwords with the exception of custom stopwords list based on
    https://github.com/RaRe-Technologies/gensim/blob/d5556ea2700333e07c8605385def94dd96fb2c94/gensim/parsing/preprocessing.py"""
    string = utils.to_unicode(string_value)
    custom_stopwords = opts["wordlist"].split(",")
    if custom_stopwords != [""]:
        stopword = [word for word in STOPWORDS if word not in custom_stopwords]
    filtered_string = " ".join(w for w in string.split() if w not in stopword)
    return filtered_string

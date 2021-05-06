"""
This module contains methods for filtering stopwords with custom stopwords
"""
from gensim import utils
from gensim.parsing.preprocessing import STOPWORDS


def remove_custom_stopwords(string_value: str, opts: dict):
    """Filters out stopwords with custom stopwords list based on
    https://github.com/RaRe-Technologies/gensim/blob/d5556ea2700333e07c8605385def94dd96fb2c94/gensim/parsing/preprocessing.py"""
    stop_word = utils.to_unicode(string_value)
    custom_stopwords = opts["wordlist"].split(",")
    if custom_stopwords == [""]:
        custom_stopwords = STOPWORDS
    filtered_string = " ".join(w for w in stop_word.split() if w not in custom_stopwords)
    return filtered_string

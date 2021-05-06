"""This module contains method to filter out stopwords."""
import gensim
from gensim.parsing.preprocessing import remove_stopwords


def remove_default_stopwords(string_value):
    """Filter out stopwords."""
    filtered_string = remove_stopwords(string_value)
    return filtered_string

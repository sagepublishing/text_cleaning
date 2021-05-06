"""This module contains method to filter out multiple whitespaces."""
import gensim
from gensim.parsing.preprocessing import strip_multiple_whitespaces


def strip_whitespaces(string_value):
    """Filters out multiple whitespaces."""
    filtered_string = strip_multiple_whitespaces(string_value)
    return filtered_string

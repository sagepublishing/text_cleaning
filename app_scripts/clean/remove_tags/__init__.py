"""This module contains method to remove tags and markup."""
import gensim
from gensim.parsing.preprocessing import strip_tags


def remove_tags(string_value):
    """Removes all the tags and markup e.g. <p> </p>."""
    return strip_tags(string_value)

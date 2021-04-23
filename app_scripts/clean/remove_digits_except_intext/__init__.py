"""This module contains method for removing digits except if digit present as a text."""
import re

# testing whether the transformation shows as out of date


def remove_digits_except_intext(string_value):
    """
    Removing digits except digits present in text.
    :param string_value: source string
    :return: filtered string
    """
    return re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", string_value)


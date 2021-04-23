"""This module contains method for removing digits present as a text."""
import re

# testing whether the transformation shows as out of date


def remove_digits_only_intext(string_value):
    """
    Only removing digits present as a text.
    :param string_value: source string
    :return: filtered string
    """
    pattern = re.compile(r"\d*([^\d\W]+)\d*")
    return pattern.sub(r"\1", string_value)

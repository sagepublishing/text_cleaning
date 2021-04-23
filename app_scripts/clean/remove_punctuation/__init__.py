"""This module contains method for removing punctuation."""
import string

translator = str.maketrans("", "", string.punctuation)


def remove_punctuation(string_value):
    """
    Removing punctuation from string.
    :param string_value: source string
    :return: filtered string
    """
    return string_value.translate(translator)

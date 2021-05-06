"""This module contains method for removing digits from string."""
from string import digits

# testing whether the transformation shows as out of date
translator = str.maketrans("", "", digits)


def remove_digits(string_value):
    """
    removing digits from string
    :param string_value: source string
    :return: filtered string
    """
    return string_value.translate(translator)

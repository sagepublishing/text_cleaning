"""This module contains method for removing punctuation except
    punctuation present in wordList."""
import string


def remove_punctuation_except(string_value: str, opts: dict):
    """
    Removing punctuation except punctuation present in wordList
    :param string_value: source string
    :param opts: source dictionary
    :return: filtered string
    """
    punct = string.punctuation
    chars_to_remove = opts["wordlist"].split(" ")
    set_of_char = set(chars_to_remove)
    punct = "".join([c for c in punct if c not in set_of_char])
    translator = str.maketrans("", "", punct)
    return string_value.translate(translator)

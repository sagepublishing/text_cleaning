"""This module contains method to replace all digits in ``text`` str
with ``replace_with`` str"""
# source: https://github.com/jfilter/clean-text/


def replace_word_breaks(string_value: str):
    """Replace all digits in ``text`` str with ``replace_with`` str,
    i.e., 123.34 to 000.00"""
    return string_value.replace("- ", "")

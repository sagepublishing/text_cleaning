"""This module contains method to replace all digits
in ``text`` str with ``replace_with`` str"""
# source: https://github.com/ShailChoksi/text2digits

from text2digits import text2digits


def convert_word_digits(string_value: str):
    """
    Replace all digits in ``text`` str with ``replace_with`` str,
     i.e., 123.34 to 000.00
    """
    t2d = text2digits.Text2Digits()
    return t2d.convert(string_value)

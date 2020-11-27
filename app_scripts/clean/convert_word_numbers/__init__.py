# source: https://github.com/ShailChoksi/text2digits

from text2digits import text2digits

def convert_word_digits(inStr: str, opts: dict):
    """Replace all digits in ``text`` str with ``replace_with`` str, i.e., 123.34 to 000.00"""
    return t2d.convert(inStr)
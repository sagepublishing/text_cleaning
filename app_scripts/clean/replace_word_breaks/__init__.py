# source: https://github.com/jfilter/clean-text/


def replace_word_breaks(inStr: str):
    """Replace all digits in ``text`` str with ``replace_with`` str, i.e., 123.34 to 000.00"""
    return inStr.replace("- ", "")

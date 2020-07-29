# source: https://github.com/jfilter/clean-text/

import re

def replace_digits(inStr: str, opts: dict):
    """Replace all digits in ``text`` str with ``replace_with`` str, i.e., 123.34 to 000.00"""
    return re.sub(r"\d", opts['token'], inStr)
"""This module contains method for removing words shorter than s."""
import gensim
from gensim.parsing.preprocessing import strip_short


def remove_short(string_value: str, opts: dict):
    """Remove words that are shorter than s."""
    return strip_short(string_value, minsize=opts["minsize"])

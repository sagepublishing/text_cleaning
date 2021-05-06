"""This module contains method for removing pattern entered by the user.
   source: https://www.datacamp.com/community/tutorials/
        stemming-lemmatization-python
"""
import re


def remove_pattern(string_value: str, opts: dict):
    """Remove pattern entered by the user"""

    string = opts["string"].split(",")[0]
    return string_value.replace(string, "")

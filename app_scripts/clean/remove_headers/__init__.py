"""This module contains method for removing headers."""
import nltk


def remove_headers(string_value):
    """Removes the first line"""
    sent_text = nltk.sent_tokenize(string_value)
    return "\n".join(sent_text[1:])

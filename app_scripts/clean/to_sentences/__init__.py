"""This module contains method to return paragraph in sentences."""
import nltk


def to_sentences(string_value):
    """
    Return paragraph in sentences.
    :param string_value: raw text
    :return: str
    """
    sent_text = nltk.sent_tokenize(string_value)
    return "\n".join(sent_text)

"""This module contains method to return stem words in text using gensim."""
import gensim
from gensim.parsing.preprocessing import stem_text


def stem_words(string_value):
    """Stems words in text using gensim."""
    return stem_text(string_value)

"""This module consists of method to return stem words in text."""
# source:
# https://www.datacamp.com/community/tutorials/stemming-lemmatization-python

from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
import nltk
nltk.download("punkt")


lancaster = LancasterStemmer()


def stem_words_lancaster(string_value):
    """Stems words in text."""
    token_words = word_tokenize(string_value)
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(lancaster.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

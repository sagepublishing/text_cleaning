"""This module contains method for Summarizing sentences using nltk."""
# source:
# https://medium.com/@gaurav5430/using-nltk-for-lemmatizing-sentences-c1bfff963258


import spacy

nlp = spacy.load("en_core_web_sm")


def lemmatize_sentence_spacy(string_value):
    """
    lemmatize sentences using spacy
    :param string_value: source string
    :return: filtered string
    """
    doc = nlp(string_value)
    tokens = []
    for token in doc:
        if token.lemma:
            tokens.append(token.lemma_)
    return " ".join(tokens)

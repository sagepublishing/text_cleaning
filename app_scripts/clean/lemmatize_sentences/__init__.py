"""
This module contains methods for converting nltk tag to wordnet tag
"""
# source:
# https://medium.com/@gaurav5430/using-nltk-for-lemmatizing-sentences-c1bfff963258

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

""" function to convert nltk tag to wordnet tag
"""


def nltk_tag_to_wordnet_tag(nltk_tag):
    """
    lemmatize sentence using nltk_tag
    :param nltk_tag:
    :return:
    """
    if nltk_tag.startswith("J"):
        return wordnet.ADJ
    elif nltk_tag.startswith("V"):
        return wordnet.VERB
    elif nltk_tag.startswith("N"):
        return wordnet.NOUN
    elif nltk_tag.startswith("R"):
        return wordnet.ADV
    else:
        return None


def lemmatize_sentence(string_value):
    """
    tokenize the string and find the POS tag for each token
    :param string_value: source string
    :return: filtered string
    """
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(string_value))
    # tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            # if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:
            # else use the tag to lemmatize the token
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)


print(lemmatize_sentence("They bought them some apples"))

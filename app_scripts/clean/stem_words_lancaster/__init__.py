# source: https://www.datacamp.com/community/tutorials/stemming-lemmatization-python

import nltk
nltk.download('punkt')
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

lancaster = LancasterStemmer()

def stem_words_lancaster(inStr):
	"""Stems words in text."""
	token_words = word_tokenize(inStr)
	stem_sentence = []
	for word in token_words:
		stem_sentence.append(lancaster.stem(word))
		stem_sentence.append(" ")
	return "".join(stem_sentence)

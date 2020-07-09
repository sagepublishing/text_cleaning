import gensim
from gensim.parsing.preprocessing import stem_text

def stem_words(inStr):
	"""Stems words in text."""
	return stem_text(inStr)
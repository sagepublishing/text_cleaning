import gensim
from gensim.parsing.preprocessing import stem_text

def stem_words(inStr):
	"""Stems words in text using gensim."""
	return stem_text(inStr)

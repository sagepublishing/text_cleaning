import gensim
from gensim.parsing.preprocessing import remove_stopwords

def remove_default_stopwords(inStr):
	"""Filters out stopwords."""
	filtered_string = remove_stopwords(inStr)
	return filtered_string

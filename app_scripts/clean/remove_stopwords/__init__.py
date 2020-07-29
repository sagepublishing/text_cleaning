import gensim
from gensim.parsing.preprocessing import remove_stopwords

def remove_stopwords(inStr):
	"""Filters out stopwords."""
	filtered_string = strip_multiple_whitespaces(inStr)
	return filtered_string
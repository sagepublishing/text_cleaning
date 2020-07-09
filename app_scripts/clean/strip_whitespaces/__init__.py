import gensim
from gensim.parsing.preprocessing import strip_multiple_whitespaces

def strip_whitespaces(inStr):
	"""Filters out stopwords."""
	filtered_string = strip_multiple_whitespaces(inStr)
	return filtered_string
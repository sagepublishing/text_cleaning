import gensim
from gensim.parsing.preprocessing import strip_tags

def remove_tags(inStr):
	"""Removes all the tags and markup e.g. <p> </p>."""
	return strip_tags(inStr)
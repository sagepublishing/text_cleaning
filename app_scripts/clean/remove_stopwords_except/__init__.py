from gensim import utils
from gensim.parsing.preprocessing import STOPWORDS

def remove_stopwords_except(inStr: str, opts: dict):
	"""Filters out stopwords with the exception of custom stopwords list based on 
	https://github.com/RaRe-Technologies/gensim/blob/d5556ea2700333e07c8605385def94dd96fb2c94/gensim/parsing/preprocessing.py"""
	s = utils.to_unicode(inStr)
	custom_stopwords = opts['wordlist'].split(',')
	if custom_stopwords != ['']:
		STOPWORDS = [word for word in STOPWORDS if word not in custom_stopwords]
	filtered_string = " ".join(w for w in s.split() if w not in STOPWORDS)
	return filtered_string


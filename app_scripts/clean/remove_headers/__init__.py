import nltk

def remove_headers(inStr):
	"""Removes the first line"""
	sent_text = nltk.sent_tokenize(inStr)
	return ("\n").join(sent_text[1:])

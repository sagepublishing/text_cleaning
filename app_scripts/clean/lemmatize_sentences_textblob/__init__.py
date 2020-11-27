# source: https://textblob.readthedocs.io/en/dev/quickstart.html

from textblob import Word


def lemmatize_sentence_textblob(inStr):
	words = inStr.split(' ')
	tokens = []
	for word in words:
		w = Word(word)
		tokens.append(w.lemmatize())
	return " ".join(tokens)




import nltk


def to_sentences(inStr):
	sent_text = nltk.sent_tokenize(inStr)
	return ("\n").join(sent_text)



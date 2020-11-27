import string

def remove_punctuation_except(inStr: str, opts: dict):
	punct = string.punctuation
	chars_to_remove = opts['wordlist'].split(' ')
	sc = set(chars_to_remove)
	punct = ''.join([c for c in punct if c not in sc])
	translator=str.maketrans('','',punct)
	return inStr.translate(translator)


#print(remove_punctuation_except("Hi, how have you been? All good, I hope....!", {"wordlist" : "? ,"}))    

import gensim
from gensim.parsing.preprocessing import strip_short

def remove_short(inStr: str, opts: dict):
	"""Remove words that are shorter than s."""
	return strip_short(inStr, minsize=opts['minsize'])
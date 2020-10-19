# source: https://www.datacamp.com/community/tutorials/stemming-lemmatization-python

import re


def remove_pattern(inStr: str, opts: dict):
	"""Remove pattern entered by the user"""

	string = opts['string'].split(',')[0]	
	return inStr.replace(string, "")


def remove_footers(inStr: str, opts: dict):
	"""Removes the first line"""
	n = int(opts['footer_lines'])
	sent_text = inStr.split('\n')
	#print(sent_text[-4])
	return ("\n").join(sent_text[:-(n+1)])


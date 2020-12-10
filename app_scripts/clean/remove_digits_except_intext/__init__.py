import re
#testing whether the transformation shows as out of date    


def remove_digits_except_intext(inStr):
	return re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", inStr)



import re
#testing whether the transformation shows as out of date    


def remove_digits_only_intext(inStr):
	pattern = re.compile(r"\d*([^\d\W]+)\d*")
	return pattern.sub(r"\1", inStr)





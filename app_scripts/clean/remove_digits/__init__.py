from string import digits 
#testing whether the transformation shows as out of date    
translator = str.maketrans('', '', digits) 

def remove_digits(inStr):
	return inStr.translate(translator) 

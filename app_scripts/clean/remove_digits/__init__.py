from string import digits 
    
translator = str.maketrans('', '', digits) 

def remove_digits(inStr):
	return inStr.translate(translator) 
import re

def remove_URL(inStr):
    """Remove URLs from a sample string"""
    string = re.sub(r"http\S+", "", inStr)
    string = re.sub(r"www.\S+", "", string)
    return string


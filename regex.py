import re 

def remove_digits(s:str)->str:
    return re.sub("\d+", "", s)

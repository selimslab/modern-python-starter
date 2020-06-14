""" regex utils """
import re 

def remove_digits(s):
    """ removes digits in a string """
    return re.sub("\d+", "", s)

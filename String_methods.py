""" Important String Methods """
# 1) find("string", beg, end)
""" It return "-1" if string is not found
in given range.
It return first occurrence of string if found."""
s = "Hello everyone, Main String here."
print(s.find("Main", 0))

# 2) islower()
""" This Function return "True" if all the 
letters in the string are lower cased, 
otherwise "False"."""
# Example Code.
s = "hello"
print(s.islower())

# 2) isupper()
""" This Function return "True" if all the 
letters in the string are upper cased, 
otherwise "False"."""
# Example Code.
s = "HELLO"
print(s.isupper())

""" 3) len() = return length of the string.
    4) count("string, beg, end") = Count the occurencr of mentioned substring.
    5) center() = This is used to surround the string with a character repeated both side.
    6) isalpha() = return True when all Character of string are alphabets.
    7) isalnum() = return True when all Character of String are the combination of alphabets and numbers.
    8) join() = This Function is used to join a sequence of strings mentioned in its arguments with the string."""

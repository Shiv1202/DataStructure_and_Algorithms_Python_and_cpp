""" -----------> Day : 128 <---------------
NOTE:
Avoid using built-in functions to solve this
challenge. Implement them yourself, since
this is what you would be asked to do during
a real interview.
----------------> Question <-----------------
Implement a function that takes two strings,
s and x, as arguments and finds the first
occurrence of the string x in s. The function
should return an integer indicating the index
in s of the first occurrence of x. If there
are no occurrences of x in s, return -1.
-------------> Example <---------------
For s = "CodefightsIsAwesome" and x = "IA",
the output should be
strstr(s, x) = -1;
----------------> END <-------------------"""

# Pattern Check Function.
def strstr(s, x):
    if x not in s:
        return -1
    else:
        i = 0
        while i <= len(s) - len(x):
            if s[i:i + len(x)] == x:
                return i
            i += 1
        
# Main Function.
def main():
    s = "CodefightsIsAwesome"
    x = "IsA"
    print(strstr(s, x))


# Driver Code.
if __name__ == "__main__":
    main()
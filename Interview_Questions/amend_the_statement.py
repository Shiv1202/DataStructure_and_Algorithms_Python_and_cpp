""" -----------> Question <---------------
You have been given a string s, which is
supposed to be a sentence. However, someone
forgot to put spaces between the different
words, and for some reason they capitalized
the first letter of every word. Return the
sentence after making the following
amendments:
1) Put a single space between the words.
2) Convert the uppercase letters to lowercase.
-------------> Example <---------------
For s = "CodesignalIsAwesome", the
output should be
amendTheSentence(s) = "codesignal is awesome";
For s = "Hello", the output should be
amendTheSentence(s) = "hello".
----------------> END <-------------------"""
"""
    Basic Method using list 
"""
# Amend Function.
def amend_the_sentence(s):
    x = list(s)
    ans = x[0].lower()
    for i in range(1, len(x)):
        if x[i].islower():
            ans += x[i]
        else:
            ans += " "
            ans += x[i].lower()
    return ans

"""
    Using Re module.
"""
import re
def amend_the_sentence_re(s):
    return ' '.join(re.findall(r"[A-Za-z][a-z]*", s)).lower()
# Main Function.
def main():
    a = "HappyCoding"
    res = amend_the_sentence_re(a)
    print(res)

# Driver Code.
if __name__ == "__main__":
    main()
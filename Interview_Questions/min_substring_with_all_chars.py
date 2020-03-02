""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Question : You have two strings, s and t.
The string t contains only unique elements.
Find and return the minimum consecutive
substring of s that contains all of the
elements from t.
It's guaranteed that the answer exists.
If there are several answers, return the
one which starts from the smallest index.
************** Example ****************
For s = "adobecodebanc" and t = "abc",
the output should be
minSubstringWithAllChars(s, t) = "banc".
******** Guaranteed constraints ********
        0 ≤ s.length ≤ 100.
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""

# Min Sub String Function.
def minSubstringWithAllChars(s, t):
    result = []
    if len(s) == 0 or len(t) == 0: 
        return ""
    for i in range(len(s)):
        if s[i] in t:
            coll = set()
            for j in range(i, len(s)):
                if s[j] in t:
                    coll.add(s[j])
                    if (len(coll) == len(t)):
                        result.append(s[i:j + 1])
    if result:
        return min(result, key = len)

# Main Function.
def main():
    s = "adobecodebanc"
    t = "abc"
    r=minSubstringWithAllChars(s,t)
    print(r)

# Driver Code.
if __name__ == "__main__":
    main()
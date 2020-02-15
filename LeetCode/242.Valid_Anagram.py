""" -----------> Question <----------------
*********** 242. Valid Anagram ************
Given two strings s and t , write a function
to determine if t is an anagram of s.
*-*-*-*-*-*-*-*-*- Example 1 *-*-*-*-*-*-*-
Input: s = "anagram", t = "nagaram"
Output: true
*-*-*-*-*-*-*-*-*- Example 2 *-*-*-*-*-*-*-
Input: s = "rat", t = "car"
Output: false
NOTE:
You may assume the string contains only
lowercase alphabets.
----------------> END <-------------------"""

# Method 1
# from collections import Counter
# class Solution:
#     def isAnagram(self, s, t):
#         return Counter(s) == Counter(t)

# Method 2
# class Solution:
#     def isAnagram(self, s, t):
#         return False if len(s) != len(t) else sorted(s) == sorted(t)

# Method 3
class Solution:
    def isAnagram(self, s, t):
        word = {}

        for c in s:
            word[c] = word[c] + 1 if c in word else 1
        
        for c in t:
            if c not in word:
                return False

            word[c] = word[c] - 1

            if word[c] <= 0:
                del word[c]

        return len(word) == 0

# Main Function.
def main():
    s1 = "anagram"; s2 = "nagaram"
    s = Solution()
    print(s.isAnagram(s1, s2))

# Driver code.
if __name__ == "__main__":
    main()
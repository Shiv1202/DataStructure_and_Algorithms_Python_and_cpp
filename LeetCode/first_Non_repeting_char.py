""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
387. First Unique Character in a String
----------------> Question <-----------------
Given a string, find the first non-repeating
character in it and return it's index.
If it doesn't exist, return -1.

---------------> Examples <----------------
INPUT => s = "leetcode"
OUTPUT => return 0.
INPUT => s = "loveleetcode",
OUTPUT => return 2.
NOTE:
You may assume the string contain
only lowercase letters
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""
# Method 1
# Time Complexity : O(n^2)
# class Solution:
#     def first_unique_char(self, s):
#         for i in range(len(s)):
#             seenDuplicate = False
#             for j in range(len(s)):
#                 if s[i] == s[j] and i != j:
#                     seenDuplicate = True
#                     break
#             if not seenDuplicate:
#                 return i
#         return -1

# Method 2
# Time Complexity : O(n)
# class Solution:
#     def first_unique_char(self, s):
#         char_counter = {}
#         for i in range(len(s)):
#             if s[i] in char_counter:
#                 char_counter[i] += 1
#             else:
#                 char_counter[i] = 1
#         for i in range(len(s)):
#             if char_counter[s[i]] == 1:
#                 return i
#             break
#         return -1 

# Method 3
# Time Complexity : O(n)
class Solution:
    def first_unique_char(self, s):
        for i in range(len(s)):
            if s.index(s[i]) == s.rindex(s[i]):
                return i
        return -1
            



# Main Function.
def main():
    s = "aaabcccdeeef"
    s1 = Solution()
    result = s1.first_unique_char(s)
    print(result)

# Driver Code.
if __name__ == "__main__":
    main()
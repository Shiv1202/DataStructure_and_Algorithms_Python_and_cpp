""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
--------------> Question <---------------
3.Longest Substring Without Repeating 
Characters
****************************************
Given a string, find the length of the
longest substring without repeating
characters.
Example 1:
Input: "abcabcbb"   Output: 3 
Explanation: The answer is "abc", with
the length of 3. 
Example 2:
Input: "bbbbb"      Output: 1
Explanation: The answer is "b", with the
length of 1
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""

# Solution Class.
class Solution:
    def lengthOfLongestSubstring(self, s):
        i, j, max_len = 0, 0, 0
        d = {}
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = 1
                j += 1
                max_len = max(len(d), max_len)
            else:
                del d[s[i]]
                i += 1
        return max_len
# Main Function.
def main():
    s = "abcabcbb"
    X = Solution()
    y = X.lengthOfLongestSubstring(s)
    print(y)

# Driver Code.
if __name__ == "__main__":
    main()
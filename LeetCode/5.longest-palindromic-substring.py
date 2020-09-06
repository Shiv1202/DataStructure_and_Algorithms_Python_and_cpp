#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = left = right = 0
        max_len = 1
        for i in range(1, n):
            left, right = i - 1, i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1

                left -= 1
                right += 1
            left = i - 1
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1
        return s[start:start+max_len]


# @lc code=end


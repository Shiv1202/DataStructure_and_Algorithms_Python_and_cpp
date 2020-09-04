#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, n: int) -> bool:
        divisor = 1
        while n / divisor >= 10:
            divisor *= 10
        while n != 0:
            start = n // divisor
            last = n % 10

            if start != last:
                return False
            n = (n % divisor) // 10

            divisor  = divisor / 100
        return True
# @lc code=end


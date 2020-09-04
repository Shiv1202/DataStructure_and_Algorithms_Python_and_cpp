#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        num = list(str(abs(x)))
        num.reverse()
        c = int("".join(num))
        if c > 2 ** 31:
            return 0
        else:
            if x >= 0:
                return c
            else:
                return -c
# @lc code=end


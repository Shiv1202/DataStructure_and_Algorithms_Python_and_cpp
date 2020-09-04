#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        rom_val = {
            "I" : 1, "V" : 5, "X" : 10,
            "L" : 50, "C" : 100, "D" : 500,
            "M" : 1000
        }
        ans = 0
        for i in range(len(s) - 1):
            if rom_val[s[i]] < rom_val[s[i + 1]]:
                ans -= rom_val[s[i]]
            else:
                ans += rom_val[s[i]]
        ans += rom_val[s[-1]]
        return ans
# @lc code=end


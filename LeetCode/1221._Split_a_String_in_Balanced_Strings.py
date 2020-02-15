""" -----------> Question <----------------
* 1221. Split a String in Balanced Strings *
Balanced strings are those who have equal
quantity of 'L' and 'R' characters.
Given a balanced string s split it in the
maximum amount of balanced strings.
Return the maximum amount of splitted
balanced strings.
*-*-*-*-*-*-*-*-*- Example 1 *-*-*-*-*-*-*-
Input: s = "RLRRLLRLRL"     Output: 4
Explanation: s can be split into "RL", "RRLL",
"RL", "RL", each substring contains same
number of 'L' and 'R'.
----------------> END <-------------------"""
# Solution Class.
class Solution:
    def balancedStringSplit(self, s):
        count = 0
        output = 0
        for i in s:
            if i == "R":
                count += 1
            else:
                count -= 1
            if count == 0:
                output += 1
        return output

# Main Function.
def main():
    s1 = "RLRRLLRLRL"
    s = Solution()
    res = s.balancedStringSplit(s1)
    print(res)

if __name__ == "__main__":
    main()
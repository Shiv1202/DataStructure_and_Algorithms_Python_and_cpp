""" -----------> Question <----------------
******** 1323. Maximum 69 Number *********
Given a positive integer num consisting
only of digits 6 and 9.
Return the maximum number you can get by
changing at most one digit (6 becomes 9,
and 9 becomes 6).
*-*-*-*-*-*-*-*-*- Example 1 *-*-*-*-*-*-*-
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
----------------> END <-------------------"""

# Solution Class
class Solution:
    def maximum69Number(self, num):
        new_num=str(num).replace('6','9',1)
        return new_num
                
# Main Function.
def main():
    s = Solution()
    n = 9996
    print(s.maximum69Number(n))

# Driver Code.
if __name__ == "__main__":
    main()
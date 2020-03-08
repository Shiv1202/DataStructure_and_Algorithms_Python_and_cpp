""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Given an array arr of integers, check if
there exists two integers N and M such
that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two
indices i and j such that :
-> i != j
-> 0 <= i, j < arr.length
-> arr[i] == 2 * arr[j]
-------------> Example <---------------
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,
that is, 10 = 2 * 5.
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"""

# Solution Class.
class Solution:
    def checkIfExist(self, arr):
        d = {}
        c = 0
        for i in range(len(arr)):
            
            if arr[i] != 0:
                d[arr[i]] = arr[i] * 2
            elif arr[i] == 0:
                c = c + 1
        print(c)
        if len(d) == 0 and c >= 2:
            return True    
        for i, j in d.items():
            if (j in d.keys() and j / 2 == i):
                return True
        return False
            

# Main Function.
def main():
    a = [0,0]
    s = Solution()
    res = s.checkIfExist(a)
    print(res)

# Driver Code.
if __name__ == "__main__":
    main()
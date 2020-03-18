""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Given the array nums, for each nums[i]
find out how many numbers in the array
are smaller than it. That is, for each
nums[i] you have to count the number of
valid j's such that j!=i and 
nums[j]<nums[i].
Return the answer in an array.
-------------> Example <---------------
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"""

# Solution Class.
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        d = {}
        snums = sorted(nums)
        for i,v in enumerate(snums):
            if v not in d:
                d[v]=i       
        return [ d[n] for n in nums ] 

# Main Function.
def main():
    a = [8, 1, 2, 2, 3]
    s = Solution()
    res = s.smallerNumbersThanCurrent(a)
    print(res)

# Driver Code.
if __name__ == "__main__":
    main()
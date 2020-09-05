#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=nums1+nums2
        nums1.sort()
        x=len(nums1)
        if x%2==0:
            z=int(x/2)-1
            return (nums1[z]+nums1[z+1])/2
        else:
            return nums1[int(x/2)]  

# @lc code=end


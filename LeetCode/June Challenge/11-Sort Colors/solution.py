class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = curr = 0
        r = len(nums) - 1
        
        while curr <= r:
            if nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
            elif nums[curr] == 0:
                nums[l], nums[curr] = nums[curr], nums[l]
                l += 1
                curr += 1
            else:
                curr += 1

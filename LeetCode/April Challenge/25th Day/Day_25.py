class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        target = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= target:
                target = i
        return not target
        

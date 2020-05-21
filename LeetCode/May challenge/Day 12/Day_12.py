class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        return abs(sum(nums) - (sum(set(nums)) * 2))

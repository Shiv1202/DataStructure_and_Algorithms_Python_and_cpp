class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        final_sum = nums[0]
        for i in range(1, len(nums)):
            temp = curr_max
            curr_max = max(max(curr_max + nums[i], curr_min + nums[i]), nums[i])
            curr_min = min(min(temp + nums[i], curr_min + nums[i]), nums[i])
            if curr_max > final_sum:
                final_sum = curr_max
        return final_sum

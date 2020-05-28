class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        f = [1] * l
        temp = 1
        for i in range(1, l):
            f[i] = temp * nums[i - 1]
            temp *= nums[i - 1]
        temp = 1
        for i in range(l-2, -1, -1):
            f[i] *= temp*nums[i+1]
            temp *= nums[i + 1]
        return f

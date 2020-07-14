class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        from copy import copy
        nums.sort()
        n = len(nums)
        if n == 0: return []
        dp = [0] * n
        dp[0] = [nums[0]]
        #print(dp)
        for i in range(1, n):
            curNum = nums[i]
            maxSet = []
            for j in range(i):
                if curNum % nums[j] == 0:
                    localSet = copy(dp[j])
                    if len(localSet) > len(maxSet):
                        maxSet = localSet
            
            maxSet.append(nums[i])
            dp[i] = maxSet
            #print(dp)
        
        #print(dp)
        res = []
        for localSet in dp:
            if len(localSet) > len(res):
                res = localSet
        return res

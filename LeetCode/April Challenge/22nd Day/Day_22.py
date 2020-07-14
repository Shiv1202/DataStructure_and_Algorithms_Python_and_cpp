from collections import defaultdict 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prevSum = defaultdict(lambda : 0)
        
        count, currSum = 0, 0
        
        for num in nums:
            currSum += num
            
            if currSum == k:
                count += 1
            
            if currSum - k in prevSum:
                count += prevSum[currSum - k]
                
            prevSum[currSum] += 1
        return count
        

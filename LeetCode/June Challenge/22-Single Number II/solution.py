class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = dict(collections.Counter(nums))
        for i in count:
            if count[i] == 1:
                return i 
        

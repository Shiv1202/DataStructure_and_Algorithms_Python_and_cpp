from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = dict(Counter(nums))
        for key in d:
            if d[key] > (n // 2):
                return key
                break

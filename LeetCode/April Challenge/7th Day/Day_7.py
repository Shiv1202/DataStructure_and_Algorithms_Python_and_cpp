from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        d = dict(Counter(arr))
        count = 0
        for i in arr:
            if (i + 1) in d:
                count += 1
        return count

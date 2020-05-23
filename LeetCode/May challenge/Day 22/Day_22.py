from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        
        return "".join(sorted(s, key = lambda x: (-frequency[x], x)))

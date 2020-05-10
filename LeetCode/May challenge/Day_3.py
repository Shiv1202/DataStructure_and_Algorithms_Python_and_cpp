from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = dict(Counter(ransomNote))
        d2 = dict(Counter(magazine))
        c = 0
        for i in d1:
            if i in d2 and d1[i] <= d2[i]:
                c += 1
        if c == len(d1):
            return True
        return False

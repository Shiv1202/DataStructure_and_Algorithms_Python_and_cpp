import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        top = int(math.log(n, 2))
        bottam = int(math.log(m, 2))
        if top != bottam:
            return 0
        
        res = m
        for i in range(m + 1, n + 1):
            res &= i
        return res

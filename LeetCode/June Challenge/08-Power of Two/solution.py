class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        res = round(math.log(n, 2))
        return 2 ** res == n

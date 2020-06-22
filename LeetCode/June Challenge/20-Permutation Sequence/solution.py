class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = math.factorial(n - 1)
        nums, k = [str(i) for i in range(1, n + 1)], k - 1
        
        res = ""
        
        for i in range(1, n):
            res = res + nums.pop(k // fact)
            k = k % fact
            fact = fact // (n - i)
            
        return res + "".join(nums)

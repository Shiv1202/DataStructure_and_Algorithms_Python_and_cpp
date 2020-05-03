# Solution Class
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1) :
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

# Main Function.
def main():
    n = int(input())
    obj = Solution()
    print(obj.climbStairs(n))

# Driver Code.
if __name__ == "__main__":
    main()
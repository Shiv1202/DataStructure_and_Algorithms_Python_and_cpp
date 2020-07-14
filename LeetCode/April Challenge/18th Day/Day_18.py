class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: 
        n, m = len(grid), len(grid[0])
        
        dp = grid # Initialize Memoization table
        
        # Base Case For Row
        for j in range(1, m):
            dp[0][j] = grid[0][j] + dp[0][j - 1]
            
        # Base Case For Col
        for i in range(1, n):
            dp[i][0] = grid[i][0] + dp[i-1][0]
            
        # General Case.
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i - 1][j])
                
        return dp[n - 1][m - 1]
    

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        dp = [[float('inf')]  * (col + 1) for _ in range(row + 1)]
        
        dp[row - 1][col], dp[row][col - 1] = 1, 1
        
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
                
        return dp[0][0]

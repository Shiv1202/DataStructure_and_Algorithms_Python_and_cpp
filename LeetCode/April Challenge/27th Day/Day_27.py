class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        max_area = 0
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0 or matrix[i - 1][j - 1] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                    max_area = max(max_area, dp[i][j])
        return max_area * max_area
    
               

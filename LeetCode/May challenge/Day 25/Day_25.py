class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        row, col = len(A), len(B)
        
        line_count = [[0 for _ in range(col + 1)] for x in range(row + 1)]
        
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if A[i - 1] == B[j - 1]:
                    line_count[i][j] = line_count[i - 1][j - 1] + 1
                else:
                    line_count[i][j] = max(line_count[i - 1][j], line_count[i][j - 1])
                
        return line_count[row][col]

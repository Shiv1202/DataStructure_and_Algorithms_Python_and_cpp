class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans, row, col = 0, len(matrix), len(matrix[0])
        for i in range(col):
            ans += matrix[row - 1][i]
        print(ans)
        for i in range(row):
            ans += matrix[i][col - 1]
        print(ans)
        ans = ans - matrix[row - 1][col - 1]
        print(ans)
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(matrix[i + 1][j + 1], matrix[i][j + 1], matrix[i + 1][j])
                else:
                    matrix[i][j] = 0
                ans = ans + matrix[i][j]
        return ans

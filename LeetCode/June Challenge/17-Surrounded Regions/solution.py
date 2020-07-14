class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 0
        
        row, col = len(board), len(board[0])
        
        
        def helper(i, j):
            if i >= 0 and i < row and j >= 0 and j < col:
                if board[i][j] == "O":
                    board[i][j] = "-"
                    helper(i + 1, j)
                    helper(i - 1, j)
                    helper(i, j + 1)
                    helper(i, j - 1)
        
        # To Change left and right border "O" to "-"
        for i in range(row):
            helper(i, 0)
            helper(i, col - 1)
        
        # To Change top and bottam border "O" to "-"
        for i in range(col):
            helper(0, i)
            helper(row - 1, i)
            
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "-":
                    board[i][j] = "O"

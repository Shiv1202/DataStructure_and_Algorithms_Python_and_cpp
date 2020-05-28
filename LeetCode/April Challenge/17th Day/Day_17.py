class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_island = 0
        if not grid:
            return 0
        # Helper Function.
        def snikit(i, j):
            """
            Verify boundary conditions.
            """
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = 0
                """
                Recursive call for L, R, U, D.
                """
                snikit(i + 1, j)
                snikit(i - 1, j)
                snikit(i, j + 1)
                snikit(i, j - 1)
        
        #We have to visit ever node of graph 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    number_of_island += 1
                    snikit(i, j)
        
        return number_of_island

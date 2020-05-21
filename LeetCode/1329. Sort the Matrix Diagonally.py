class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # If length of mat is less then 2 
        if len(mat) < 2: return sorted(mat)[::-1]
        
        n = len(mat)
        n1 = len(mat[0])
        
        # for upper half.
        for i in range(1, n1):
            tra, row, col = [], 0, i
            
            # Get digonals of upper half
            while col < n1 and row < n:
                tra.append(mat[row][col])
                row += 1
                col += 1
                
            # sorting
            x = sorted(tra)[::-1]
            
            # Inserting back in matrix
            row = 0
            col = i
            while col < n1 and x:
                mat[row][col] = x.pop()
                row += 1
                col += 1
        
        # For left lower half
        for j in range(n):
            tra, row, col = [], j, 0
            
            # Get digonals of left lower half
            while row < n and col < n1:
                tra.append(mat[row][col])
                row += 1
                col += 1
                
            # Sorting
            x = sorted(tra)[::-1]
            
            # Inserting back in matrix
            col = 0
            row = j
            while row < n and x:
                mat[row][col] = x.pop()
                row += 1
                col += 1
        return mat

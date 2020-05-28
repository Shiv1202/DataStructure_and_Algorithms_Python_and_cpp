# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        if not BinaryMatrix.dimensions(binaryMatrix):
            return -1
        x = BinaryMatrix.dimensions(binaryMatrix)
        n, m = x[0], x[1]
        row, col = 0, m - 1
        
        while row < n and col >= 0:
            if BinaryMatrix.get(binaryMatrix, row, col) == 1:
                col -= 1
            else:
                row += 1
        return col + 1 if col != m - 1 else -1
        

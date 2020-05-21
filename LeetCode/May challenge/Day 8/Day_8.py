class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        
        for p in range(n):
            if (dy*(coordinates[p][0]-coordinates[p-1][0])) != (dx*(coordinates[p][1]-coordinates[p-1][1])):
                return False
        return True

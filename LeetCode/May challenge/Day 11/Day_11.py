class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]: return image
        
        q, prevColor = [(sr, sc)], image[sr][sc]
        
        while q:
            r, c = q.pop(0)
            
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == prevColor:
                image[r][c] = newColor
                q.append((r+1, c))
                q.append((r-1, c))
                q.append((r, c+1))
                q.append((r, c-1))
        
        return image

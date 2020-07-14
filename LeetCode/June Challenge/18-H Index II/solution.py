class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n, low, high = len(citations), 0, len(citations)
        
        while low < high:
            mid = low  + (high - low) // 2
            numGreater = n - mid
            
            if numGreater <= citations[mid]:
                high = mid
            else:
                low = mid + 1
                
        return n - low

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
    
        # Function for Bineary Search
        def binary_search(arr):
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < 0:
                    high = mid - 1
                else:
                    low = mid + 1
            return len(arr) - low
            
        # Sorting the count of negative numbers in one row and after getting for all row return sum of all count.
        return sum([binary_search(arr) for arr in grid])

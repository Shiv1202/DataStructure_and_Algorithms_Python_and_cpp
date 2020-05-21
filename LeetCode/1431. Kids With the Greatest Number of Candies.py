class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        output = []
        for c in candies:
            if c + extraCandies >= max_candies:
                output.append(True)
            else:
                output.append(False)
        return output

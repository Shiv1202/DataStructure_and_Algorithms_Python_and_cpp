class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans, n = 0, len(costs) // 2
        diff = [(a - b) for a, b in costs]
        order_diff = sorted((value, i) for (i, value) in enumerate(diff))
        for value, i in order_diff[:n]:
            ans += costs[i][0]
        for value, i in order_diff[n:]:
            ans += costs[i][1]
        
        return ans

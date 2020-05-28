import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            x = heapq.nlargest(2, stones)
            if x[0] == x[1]:
                stones.remove(x[0])
                stones.remove(x[1])
            else:
                stones.remove(x[0])
                stones.remove(x[1])
                stones.append(x[0] - x[1])
        else:
            if stones: 
                return stones[0]
            else:
                return 0
        

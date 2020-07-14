from collections import deque
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dq = deque()
        self.seen = {}
        
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if len(self.dq) == 0:
            return -1
        while len(self.dq) > 0 and self.dq[0] in self.seen and self.seen[self.dq[0]] >= 2:
            self.dq.popleft()
            
        if len(self.dq) == 0:
            return -1
        
        return self.dq[0]

    def add(self, value: int) -> None:
        if value in self.seen:
            self.seen[value] += 1
        else:
            self.seen[value] = 1
            
        self.dq.append(value)
    

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

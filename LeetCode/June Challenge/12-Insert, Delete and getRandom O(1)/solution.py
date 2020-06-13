from random import choice

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.mapping = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mapping:
            return False
        self.mapping[val] = len(self.arr)
        self.arr.append(val)
        
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.mapping:
            last_val, index_to_delete = self.arr[-1], self.mapping[val]
            self.arr[index_to_delete], self.mapping[last_val] = last_val, index_to_delete
            self.arr.pop()
            
            del self.mapping[val]
            return True
        return False
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        
        return choice(self.arr)
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

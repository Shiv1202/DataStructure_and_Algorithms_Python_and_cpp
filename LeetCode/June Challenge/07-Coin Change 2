class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        changes = [0] * (amount + 1)
        changes[0] = 1
        
        for coin in coins:
            for j in range(coin, amount + 1):
                changes[j] += changes[j - coin]
        return changes[amount]

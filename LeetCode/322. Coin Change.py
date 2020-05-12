class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        changes = [float('inf')] * (amount + 1)
        changes[0] = 0
        
        for coin in coins:
            for j in range(coin, amount + 1):
                changes[j] = min(changes[j], changes[j - coin] + 1)
        return changes[amount] if changes[amount] != float('inf') else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        def rec(coins, amount):
            if amount == 0:
                return 0

            if amount in dp:
                return dp[amount]
        
            minimum = inf
            for coin in coins:
                if (amount - coin) >= 0:
                    minimum = min(minimum, rec(coins, amount - coin) + 1)
                
            dp[amount] = minimum
            return dp[amount]

        return rec(coins, amount) if rec(coins, amount) != inf else -1
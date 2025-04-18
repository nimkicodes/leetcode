class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None]* (amount+1)
        
        def dp(n):
            if n == 0:
                return 0

            if memo[n] is not None:
                return memo[n]
        
            minimum = inf
            for coin in coins:
                if (n - coin) >= 0:
                    minimum = min(minimum, dp(n - coin) + 1)
                
            memo[n] = minimum
            return memo[n]

        return dp(amount) if dp(amount) != inf else -1
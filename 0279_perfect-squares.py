class Solution:
    def numSquares(self, n: int) -> int:
        # Time complexity, O(n√n)
        # dp[x] = min number of coins to make up amount 
        dp = [inf] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            for num in range(1, isqrt(i)+1):
                dp[i] = min(dp[i], dp[i - num * num]+1)
        
        return dp[n]

        # # iterative DP (coin change)
        # coins = []
        # for num in range(1, n+1):
        #     if num * num > n:
        #         break
        #     coins.append(num * num)
        
        # # dp[x] = min number of coins to make up amount 
        # dp = [inf] * (n+1)
        # dp[0] = 0
        
        # for i in range(1, n+1):
        #     for coin in coins: 
        #         if i - coin >= 0:
        #             dp[i] = min(dp[i], dp[i-coin]+1)
        
        # return dp[n]
        
        # # recursive DP (coin change)
        # coins = []
        # for num in range(1, n+1):
        #     if num * num > n:
        #         break
        #     coins.append(num * num)
        
        # # dp[x] = min number of coins to make up amount 
        # dp = {}
        # def rec(amount):
        #     if amount == 0:
        #         return 0

        #     if amount in dp:
        #         return dp[amount]
        
        #     minimum = inf
        #     for coin in coins:
        #         if (amount - coin) >= 0:
        #             minimum = min(minimum, rec(amount - coin) + 1)
                
        #     dp[amount] = minimum
        #     return dp[amount]

        # return rec(n) 
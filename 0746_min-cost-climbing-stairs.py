class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom-up
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[n - 1], dp[n - 2])
        
        # top-down 
        # memo = [None] * len(cost)
        # def dp(n):
        #     if n < 2:
        #         return cost[n]
        #     if memo[n] is not None:
        #         return memo[n]
        #     memo[n] = cost[n] + min(dp(n-1), dp(n-2))
        #     return memo[n]

        # return min(dp(len(cost)-1), dp(len(cost)-2))
        
        # cost.append(0)
        # for i in range(len(cost)-4, -1, -1):
        #     cost[i] += min(cost[i+1], cost[i+2])
        
        # return min(cost[0], cost[1])
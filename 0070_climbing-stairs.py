class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        prev1 = 3
        prev2 = 2
        for _ in range(3, n):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return current
        
        # dp = [0] * (n+1)
        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[-1]
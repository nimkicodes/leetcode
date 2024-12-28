class Solution:
    def arrangeCoins(self, n: int) -> int:
        steps = 0
        for coin in range(1,n+1):
            n -= coin
            if n < 0:
                break
            steps += 1
        return steps

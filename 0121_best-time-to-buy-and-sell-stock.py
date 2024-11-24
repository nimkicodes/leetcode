class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # bruteforce, O(n2) time
        # constraint = (10^5)^2 -> 10^10 which is > 5x10^8, it gives TLE

        profit = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]

        if profit >= 0:
            return profit
        else:
            return 0
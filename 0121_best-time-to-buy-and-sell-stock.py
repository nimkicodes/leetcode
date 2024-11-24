class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # kadane's algorithm , O(n) time, O(1) space
        profit = 0
        buy_price = prices[0]

        for current_price in prices[1:]:
            if current_price < buy_price:
                buy_price = current_price

            profit = max(profit, current_price - buy_price)
        
        return profit

        # bruteforce, O(n2) time
        # constraint = (10^5)^2 -> 10^10 which is > 5x10^8, it gives TLE

        # profit = 0
        
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > profit:
        #             profit = prices[j] - prices[i]

        # if profit >= 0:
        #     return profit
        # else:
        #     return 0
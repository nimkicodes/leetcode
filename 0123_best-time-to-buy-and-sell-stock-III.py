class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_buy = second_buy = float("-inf")
        first_sell = second_sell = 0

        for price in prices:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, price + first_buy)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, price + second_buy)

        return second_sell
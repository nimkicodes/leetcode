class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = float(-inf)
        
        for money in accounts:
            wealth = sum(money)
            maximum = max(wealth, maximum)
        
        return maximum

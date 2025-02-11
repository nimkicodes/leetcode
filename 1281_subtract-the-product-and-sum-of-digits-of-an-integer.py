class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = [int(digits) for digits in str(n)]
        
        num_sum , num_product = 0, 1
        for digit in num:
            num_product *= digit
            num_sum += digit
        
        return num_product - num_sum
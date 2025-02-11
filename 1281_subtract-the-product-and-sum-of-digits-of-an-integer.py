class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = [int(digits) for digits in str(n)]
        num_sum = sum(num)
        
        num_product = 1
        for digit in num:
            num_product *= digit
        
        return num_product - num_sum
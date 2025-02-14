class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = sum([int(i) for i in str(x)])
        
        if x % digit_sum == 0:
            return digit_sum
        
        return -1
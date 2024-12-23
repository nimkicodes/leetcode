class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_single, sum_double = 0, 0

        for number in nums:
            if len(str(number)) == 1:
                sum_single += number 
            else:
                sum_double += number 
        
        return sum_single > sum_double or sum_single < sum_double
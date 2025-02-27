class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        current_max = current_min = 1
        
        for number in nums:
            if number == 0:
                current_max = current_min = 1
                
            current = current_max * number 
            current_max = max(current, current_min * number, number)
            current_min = min(current, current_min * number, number)

            result = max(result, current_max)
        
        return result
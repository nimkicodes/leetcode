class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for number in nums:
            if current_sum < 0:
                current_sum = 0
        
            current_sum += number 
            max_sum = max(max_sum, current_sum)
        
        return max_sum
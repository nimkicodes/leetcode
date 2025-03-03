class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = all(x <= y for x, y in zip(nums, nums[1:]))
        decreasing = all(x >= y for x, y in zip(nums, nums[1:]))
        return increasing or decreasing
    
        # increasing, decreasing = True, True
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         increasing = False 
            
        #     if nums[i] > nums[i-1]:
        #         decreasing = False
        
        # return increasing or decreasing
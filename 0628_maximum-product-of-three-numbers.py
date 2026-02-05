class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  
        
        p1 = nums[0] * nums[1] * nums[2] 
        p2 = nums[-1] * nums[-2] * nums[0]
        return max(p1,p2)
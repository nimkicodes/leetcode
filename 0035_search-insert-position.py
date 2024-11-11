class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = (left + right) // 2 # left + (right - left)/2 in C/Go for int overflow
            
            if nums[middle] == target:
                return middle
            
            elif target > nums[middle]: # left = right = middle (last state)
                left = middle + 1 

            else:
                right = middle - 1
                
        return left
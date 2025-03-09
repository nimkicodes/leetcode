class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            check = abs(nums[i]) 
            if 1 <= check <= len(nums):
                if nums[check - 1] > 0:
                    nums[check - 1] *= -1
                elif nums[check - 1] == 0:
                    nums[check - 1] = -1 * (len(nums) + 1)
        
        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i

        return len(nums) + 1


        # if all(num <= 0 for num in nums):
        #     return 1 
                       
        # nums[:] = [num for num in nums if num > 0]  
        
        # if len(nums) != 0:
        #     maximum = max(nums)
        # else:
        #     return 1

        # for num in range(1, maximum+1):
        #     if num != nums[num]:
        #         return num
        #     else:
        #         continue

        # return maximum + 1
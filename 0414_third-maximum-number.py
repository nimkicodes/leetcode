class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = max(nums)
        nums = [num for num in nums if num != first_max]

        if nums != []:
            second_max = max(nums)
        nums = [num for num in nums if num != second_max]
        
        third_max = 0
        if nums != []:
            third_max = max(nums)
            return third_max
        else:
            return first_max

        # first, second, third = float(-inf), float(-inf), float(-inf)

        # for num in nums:
        #     if num in (first, second, third):
        #         continue
            
        #     if num > first:
        #         first, second, third = num, first, second
            
        #     elif num > second:
        #         second, third = num, third
            
        #     elif num > third:
        #         third = num
            
        # return third if third != float(-inf) else first
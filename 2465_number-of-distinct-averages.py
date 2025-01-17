class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = set()
        
        i, j = 0, len(nums)-1
        while i < j: 
            averages.add( (nums[i] + nums[j]) / 2)
            i += 1
            j -= 1

        return len(averages)          
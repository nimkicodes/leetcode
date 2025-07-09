class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        
        i = 0
        for num in [0,1,2]:
            for _ in range(count[num]):
                nums[i] = num
                i += 1
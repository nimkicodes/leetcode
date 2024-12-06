class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, maximum = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maximum = max(count, maximum)
            else:
                count = 0

        return maximum
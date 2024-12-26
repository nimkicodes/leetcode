class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minimum, maximum = min(nums), max(nums)
        for number in nums:
            if number != minimum and number != maximum:
                return number
        return -1
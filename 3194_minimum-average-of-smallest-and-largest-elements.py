class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages = set()

        i, j = 0, len(nums)-1
        while i < j:
            averages.add((nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        
        return min(averages)
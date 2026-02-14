class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)): 
            d[nums[i]] = i

        nums.sort(reverse=True)
        if nums[0] >= nums[1] * 2: 
            return d[nums[0]]

        return -1
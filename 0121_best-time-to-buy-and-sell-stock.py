class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        existence = {}

        for x in nums:
            if x in existence:
                existence[x] += 1
            else:
                existence[x] = 1

        for y in nums:
            if existence[y] > (len(nums)//2):
                return y
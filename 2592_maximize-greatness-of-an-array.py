class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i = perm = result = 0

        while perm < len(nums):
            if nums[i] < nums[perm]:
                result += 1
                i += 1
            perm += 1
        
        return result 
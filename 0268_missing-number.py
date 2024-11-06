class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minimum = min(nums)
        n = len(nums)
        all_set = set(range(minimum, n+1))

        nums_set = set(nums)
        missing = all_set - nums_set

        if len(missing) == 0:
            return 0
        
        return list(missing).pop()
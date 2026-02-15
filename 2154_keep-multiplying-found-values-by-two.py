class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # O(nlogn)
        # nums.sort()
        # for num in nums:
        #     if num == original:
        #         original = original * 2 
        # return original

        # O(n)
        nums = set(nums)
        while original in nums:
            original *= 2
        return original
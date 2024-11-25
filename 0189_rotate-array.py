class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # to handle cases where k > len(nums)
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
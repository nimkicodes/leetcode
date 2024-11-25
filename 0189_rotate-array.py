class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # to handle cases where k > len(nums)
        k = k % len(nums)

        rotated = []
        rotated = nums[-k:] + nums[:-k]
        
        nums.clear()
        for i in range(len(rotated)):
            nums.append(rotated[i])
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = []
        for i in range(len(nums1)):
            if i > m - 1:
                nums1.pop()
    
        nums = nums1 + nums2
        nums.sort()
        nums1.clear()
        for i in range(len(nums)):
            nums1.append(nums[i])

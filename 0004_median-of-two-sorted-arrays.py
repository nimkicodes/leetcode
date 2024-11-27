class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged_nums = []
        median = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_nums.append(nums1[i])
                i += 1
            
            else:  
                merged_nums.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged_nums.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged_nums.append(nums2[j])
            j += 1

        # merged_nums = nums1 + nums2
        # merged_nums.sort()
 
        n = len(merged_nums)

        if n % 2 == 0:
            median = (merged_nums[n//2 - 1] + merged_nums[n//2]) / 2 
            return median
        else:
            median = merged_nums[n//2]
            return median
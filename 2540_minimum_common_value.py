class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = set(nums1)
        n2 = set(nums2)
        n = list(n1 & n2)
        if len(n) == 0:
            return -1
        else:
            return min(n)       
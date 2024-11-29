class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counter = defaultdict(int)
        for x in nums1:
            counter[x] += 1
        
        intersection = []
        for y in nums2:
            if y in counter and counter[y] > 0:
                intersection.append(y)
                counter[y] -= 1 
        
        return intersection
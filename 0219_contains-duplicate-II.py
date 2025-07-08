class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        check = {}

        for i in range(len(nums)):
            if nums[i] in check and abs(i - check[nums[i]]) <= k:
                return True
            check[nums[i]] = i 
            
        return False
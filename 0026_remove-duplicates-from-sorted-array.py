class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        isDuplicate = {}
        for x in nums:
            isDuplicate[x] = True
        nums.clear()
        for k in isDuplicate.keys():
            nums.append(k)
        return len(nums)
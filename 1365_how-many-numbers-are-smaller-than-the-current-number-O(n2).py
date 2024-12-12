class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j] and j!=i:
                    count += 1
            result.append(count)
            count = 0
        
        return result
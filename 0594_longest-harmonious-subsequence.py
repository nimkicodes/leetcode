class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0 
        
        for num in count:
            if num+1 in count:
                result = max(count[num] + count[num+1], result)

        return result
class Solution:
    def countElements(self, nums: List[int]) -> int:
        n1 = min(nums)
        n2 = max(nums)

        count = 0 
        for number in nums: 
            if number > n1 and number < n2:
                count += 1
                
        return count
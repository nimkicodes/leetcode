class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n), O(1)
        # xor works bitwise and commutative, A xor A = 0, A xor 0 = A
        xor = nums[0]
        
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        
        return xor 
        
        # O(n2), O(1)
        # for n in nums:
        #     if nums.count(n) == 1:
        #         return n
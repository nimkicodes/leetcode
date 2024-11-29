class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n), O(1)
        # xor works bitwise and commutative, A xor A = 0, A xor 0 = A
        xor = nums[0]
        
        for x in nums[1:]:
            xor = xor ^ x
        
        return xor 

        # O(n), O(n)
        # dictionary 

        # counter = defaultdict(int)
        # for x in nums:
        #     counter[x] += 1

        # for k,v in counter.items():
        #     if v == 1:
        #         return k
        
        # O(nlogn), O(1)
        # nums.sort()
        # for i in range(0, len(nums), 2):
        #     if i+1 >= len(nums) or nums[i] != nums[i+1]:
        #         return nums[i]
        
        # O(n2), O(1)
        # for n in nums:
        #     if nums.count(n) == 1:
        #         return n
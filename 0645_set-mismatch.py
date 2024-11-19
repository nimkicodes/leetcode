class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dict_set = {}

        for x in nums:
            if x in dict_set:
                dict_set[x] += 1
            else:
                dict_set[x] = 1
        
        for y in range(1, len(nums)+1):
            if y not in dict_set:
                missing = y
            elif dict_set[y] == 2:
                duplicate = y
        
        return [duplicate, missing]
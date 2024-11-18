class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        full_set = set([x for x in range(1, len(nums)+1)])
        missing = list(full_set - nums_set).pop()

        dict_set = {}

        for x in nums:
            if x in dict_set:
                dict_set[x] += 1
            else:
                dict_set[x] = 1

        for k in dict_set.keys():
            if dict_set[k] == 2:
                return [k, missing]
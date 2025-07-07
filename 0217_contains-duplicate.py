class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

        # count = Counter(nums)

        # for count in count.values():
        #     if count > 1:
        #         return True
        
        # return False 
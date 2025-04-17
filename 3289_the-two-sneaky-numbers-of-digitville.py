class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [digit for digit, count in Counter(nums).items() if count == 2]
        
        # digitville = defaultdict(int)
        # for num in nums:
        #     digitville[num] += 1
        
        # result = []
        # for digit, count in digitville.items():
        #     if count == 2:
        #         result.append(digit)

        # return result
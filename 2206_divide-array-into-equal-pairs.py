class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        return all(v%2 == 0 for v in counter.values())
        # return not any(v%2 != 0 for v in counter.values())

        # for v in counter.values():
        #     if v%2 != 0:
        #         return False
        # return True
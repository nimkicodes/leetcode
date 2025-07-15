class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        max_degree = max(frequency.values())
        elements = [k for k in frequency.keys() if frequency[k] == max_degree]

        reversed_nums = nums[::-1]
        result = float('inf')
        
        for element in elements:
            first_index = nums.index(element)
            last_index = len(nums) - 1 - reversed_nums.index(element)

            current = last_index - first_index + 1
            result = min(result, current)
        
        return result
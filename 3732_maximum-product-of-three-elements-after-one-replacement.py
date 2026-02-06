class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        MAX = 100000

        max1, max2 = nums[-1], nums[-2]
        min1, min2 = nums[0], nums[1]

        cases = [
            MAX * max1 * max2,     # +MAX with two largest
            MAX * min1 * min2,     # +MAX with two smallest (negatives)
            -MAX * max1 * min1,    # -MAX with mixed signs
            -MAX * max2 * min2     # -MAX with another mixed option
        ]

        return max(cases)
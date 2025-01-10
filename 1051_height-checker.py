class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        result = 0
        for height, expected in zip(heights, expected):
            if height != expected:
                result += 1

        return result
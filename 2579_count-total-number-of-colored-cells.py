class Solution:
    def coloredCells(self, n: int) -> int:
        result = 1
        for cell in range(1, n):
            result += cell * 4
        return result
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        result = [[x,y] for y in range(cols) for x in range(rows)]
        result.sort(key=lambda x: abs(x[0]-rCenter) + abs(x[1]-cCenter))
        return result
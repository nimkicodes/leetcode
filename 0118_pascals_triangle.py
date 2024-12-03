class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        pascals_triangle = self.generate(numRows-1)
        
        prev_row = pascals_triangle[-1]
        new_row = [1]

        for i in range(len(prev_row)-1):
            new_row.append(prev_row[i] + prev_row[i+1])
        new_row.append(1)
        
        pascals_triangle.append(new_row)
        return pascals_triangle
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        #important: when reshaping is not possible
        if len(mat) * len(mat[0]) != r * c:
            return mat 

        #2D to 1D array flaten
        flat = []
        for row in mat:
            for val in row: 
                flat.append(val)

        #1D to 2D trasnform and return 
        result = []
        index = 0

        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(flat[index])
                index += 1
            result.append(new_row)

        return result 
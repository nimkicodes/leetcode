class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row_check = column_check = True

        for row in matrix:
            if len(set(row)) != len(matrix):
                row_check = False

        for column in zip(*matrix):
            if len(set(column)) != len(matrix):
                column_check = False
        
        return row_check and column_check

        # zip(*matrix) transposes a matrix. 
        # list(zip(*matrix)) will print the transposed in list of tuples format.
        # list(map(list,zip(*matrix))) will print the transposed matrix in the 2D array format.
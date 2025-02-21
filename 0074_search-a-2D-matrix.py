class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(m * n) : bruteforce (this gets accepted too somehow)
        # for row in matrix:
        #     for number in row:
        #         if number == target:
        #             return True 
        
        # return False 

        # O(log(m * n)) : binary search in sorted 2D matrix 
        num_rows, num_cols = len(matrix), len(matrix[0])
        left, right = 0, (num_rows * num_cols) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // num_cols 
            col = mid % num_cols 

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left = mid + 1
            
            else:
                right = mid - 1

        return False
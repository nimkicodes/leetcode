class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0
        
        for i in range(n):
            result += mat[i][i] + mat[n-1-i][i]
        
        return result if n%2 == 0 else result - mat[n//2][n//2]
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # bottom-up memoization
        m, n = len(grid), len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        for i in range(1, n):
            grid[0][i] += grid[0][i-1]  

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
    
        # top-down
        # m, n = len(grid), len(grid[0])
        # def minPath(i, j):
        #     if i == 0 and j == 0:
        #         return grid[0][0]
        #     if i < 0 or j < 0:
        #         return float('inf')
        #     return grid[i][j] + min(minPath(i-1, j), minPath(i, j-1))
        
        # return minPath(m-1,n-1)

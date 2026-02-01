class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:        
        rows = len(grid)
        cols = len(grid[0])

        land, shared = 0, 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: 
                    land += 1
                    if j+1 < cols and grid[i][j+1] == 1: 
                        shared += 1
                    elif i-1 >= 0 and grid[i-1][j] == 1:
                        shared += 1
        
        return 4 * land - 2 * shared
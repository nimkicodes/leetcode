class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start = 0 
        end = n-1
        
        water = 0
        max_water = 0

        if n == 1:
            return height[0]

        while start < end:
            if height[start] < height[end]:
                water = height[start]*(end-start)
                start += 1
            else:
                water = height[end]*(end-start)
                end -=1

            if water > max_water:
                max_water = water

        return max_water       
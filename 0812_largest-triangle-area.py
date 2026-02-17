class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        max_area = 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    area = abs((x2-x1) * (y3-y1) - (y2-y1) * (x3-x1))
                    max_area = max(max_area, area)

        return max_area/2.0
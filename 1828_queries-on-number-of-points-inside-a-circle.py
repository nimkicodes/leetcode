class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = [0] * len(queries) 
        
        for i, (h, k, radius) in enumerate(queries):
            count = 0
            for x, y in points:
                if (x-h)**2 + (y-k)**2 <= radius**2:
                    count += 1   
            answer[i] = count
        
        return answer
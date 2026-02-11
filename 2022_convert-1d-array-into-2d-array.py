class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        result = []
        index = 0 

        for i in range(m):
            new_row = []
            for j in range(n):
                new_row.append(original[index])
                index += 1
            result.append(new_row) 
        
        return result
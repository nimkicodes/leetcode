class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tuple_map = []
        
        for i in range(len(s)):
            tuple_map.append((indices[i], s[i]))

        tuple_map.sort()
        
        result = ""
        for i in range(len(s)):
            result += tuple_map[i][1]
        
        return result   
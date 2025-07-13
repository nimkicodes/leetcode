class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        map_s, map_t = {}, {}
        
        for i in range(len(s)):
            map_s[s[i]] = i
        
        for i in range(len(t)):
            map_t[t[i]] = i
        
        diff = 0
        for char in s:
            diff += abs(map_s[char] - map_t[char])
        return diff 
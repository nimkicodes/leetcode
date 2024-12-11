class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        dict_s = defaultdict(int)
        for x in s:
            dict_s[x] += 1

        dict_t = defaultdict(int)
        for x in t:
            dict_t[x] += 1
        
        return dict_s == dict_t
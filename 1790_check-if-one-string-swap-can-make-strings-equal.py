class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
            
        if len(s1) != len(s2) or set(s1) != set(s2):
            return False 

        difference = [ index for index in range(len(s1)) if s1[index] != s2[index] ] 
        
        if len(difference) == 2:
            s1 = list(s1)
            s1[difference[0]], s1[difference[1]] = s1[difference[1]], s1[difference[0]]

        return s1 == list(s2) 
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1, 
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        integer = 0

        for i in range(len(s)):
            if i == len(s) -1 or roman[s[i]] >= roman[s[i+1]]:
                integer += roman[s[i]]
            else:
                integer -= roman[s[i]]
        
        return integer
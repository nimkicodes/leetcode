class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy_string = ""
        char_count = 0

        for i in range(len(s)):
            if i> 0 and s[i] == s[i-1]:
                char_count += 1
            else:
                char_count = 1
            
            if char_count < 3:
                fancy_string += s[i]
    
        return fancy_string
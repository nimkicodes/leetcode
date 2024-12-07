class Solution:
    def maxPower(self, s: str) -> int:
        count, power = 1, 1  
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:  
                count += 1
                power = max(power, count)
            else:
                count = 1  
        
        return power
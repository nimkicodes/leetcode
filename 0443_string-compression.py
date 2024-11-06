class Solution:
    def compress(self, chars: List[str]) -> int:
        start = 0  
        end = 0
        n = len(chars)  
        s = ""
        
        for end in range(n):
            if end == n-1 or chars[end] != chars[end + 1]:
                s += chars[end]
                group_length = end - start + 1  
                
                if group_length > 1:
                    s += str(group_length)
                
                start = end + 1
    
        for i in range(len(s)):
            chars[i] = s[i]
        
        return len(s)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        check = Counter(s)

        for i in range(len(s)):
            if check[s[i]] == 1:
                return i
        
        return -1
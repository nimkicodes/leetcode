class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        check = Counter(s)

        for i in range(len(s)):
            if check[s[i]] == 1:
                return i
        
        return -1
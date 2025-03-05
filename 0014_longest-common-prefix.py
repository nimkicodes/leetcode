class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
        def commonPrefixOfPair(s1: str, s2: str) -> str:
            prefix = []
            i = 0
            while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
                prefix.append(s1[i])
                i += 1
            return "".join(prefix)
   
        longest = strs[0]
        for i in range(1, len(strs)):
            current = commonPrefixOfPair(strs[i], strs[i-1])
            longest = current if len(current) < len(longest) else longest
        
        return longest

        # prefix = []
        # for char in zip(*strs):  
        #     if len(set(char)) == 1:
        #         prefix.append(char[0])
        #     else:
        #         break
        
        # return "".join(prefix)
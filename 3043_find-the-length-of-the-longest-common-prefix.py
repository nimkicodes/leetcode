# declare the data structure for the trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
    
    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def findLengthOfPrefix(self, word):
        node = self #root
        prefix = 0
        for char in word:
            if char not in node.children:
                return prefix
            prefix += 1
            node = node.children[char]
        return prefix

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        root = TrieNode()
        for num in arr1:
            root.insert(str(num))
        
        longest = 0
        for num in arr2:
            longest = max(longest, root.findLengthOfPrefix(str(num)))

        return longest 

        # def commonPrefixOfPair(s1: str, s2: str) -> int:
        #     i = 0 
        #     limit = min(len(s1), len(s2))
        #     while i < limit and s1[i] == s2[i]:
        #         i += 1 
        #     return i 

        # a1 = [ str(item) for item in arr1 ]
        # a2 = [ str(item) for item in arr2 ]
        # a1.sort()
        # a2.sort()
        
        # i, j = 0, 0
        # longest = 0
        # while i < len(a1) and j < len(a2):
        #     longest = max (longest, commonPrefixOfPair(a1[i], a2[j]))

        #     if a1[i] < a2[j]:
        #         i += 1
        #     else:
        #         j += 1
                
        # return longest 
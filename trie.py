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

    def findPrefix(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
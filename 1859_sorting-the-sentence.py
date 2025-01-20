class Solution:
    def sortSentence(self, s: str) -> str:
        pairs = [ [x[:-1], int(x[-1])] for x in s.split() ] 
        pairs.sort(key = lambda x:x[1])
        shuffled = [ pair[0] for pair in pairs ]
        return " ".join(shuffled)
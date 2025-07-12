class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = Counter(t) - Counter(s)
        return list(diff.keys())[0]
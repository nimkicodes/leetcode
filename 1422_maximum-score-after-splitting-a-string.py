class Solution:
    def maxScore(self, s: str) -> int:
        maximum = float(-inf)
        for i in range(1, len(s)):
            score = s[:i].count('0') + s[i:].count('1')
            maximum = max(maximum, score)
        return maximum
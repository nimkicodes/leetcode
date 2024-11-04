class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for x in s:
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False
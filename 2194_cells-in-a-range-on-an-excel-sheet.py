class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, c2, r1, r2 = ord(s[0]), ord(s[3]), int(s[1]), int(s[4])
        return [ chr(column) + str(row) for column in range(c1, c2+1) for row in range(r1, r2+1)]
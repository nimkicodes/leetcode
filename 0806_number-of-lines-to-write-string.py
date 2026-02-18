class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        current = 0

        for ch in s:
            w = widths[ord(ch)-ord('a')]
            if current + w > 100:
                lines += 1
                current = w
            else:
                current += w
        
        return [lines, current]
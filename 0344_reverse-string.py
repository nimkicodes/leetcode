class Solution:
    def reverseString(self, s: List[str]) -> None:
        # O(n) time, O(1) space
        # s.reverse()

        # O(n) time, O(1) space 
        # just more labour, that's it
        start, end = 0, len(s)-1

        while start < end:
            s[start] , s[end] = s[end], s[start]
            start += 1
            end -= 1
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n

        while start < end:
            check = (start + end) // 2
        
            if isBadVersion(check) == False:
                start = check + 1
            
            else:
                end = check

        return start
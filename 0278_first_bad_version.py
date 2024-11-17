# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        ans = 0
        while start <= end:
            check = (start + end) // 2
            val = isBadVersion(check)
            if val == False:
                ans = check 
                start = check + 1
            else:
                end = check - 1

        return ans
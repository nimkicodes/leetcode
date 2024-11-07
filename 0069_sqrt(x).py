class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0,x+1):
            if x >= (i**2) and x < (i+1)**2:
                return i
        return 0
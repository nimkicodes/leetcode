class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        elif n%2 == 0:
            for i in range(31):
                if pow(2,i) == n:
                    return True
        
        return False
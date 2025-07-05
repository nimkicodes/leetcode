class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        
        elif n%3 == 0:
            for i in range(31):
                if pow(3,i) == n:
                    return True
        
        return False
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n & n-1) == 0 and (n-1)%3 == 0
        
        # if n == 1:
        #     return True
        
        # elif n%4 == 0:
        #     for i in range(31):
        #         if pow(4,i) == n:
        #             return True

        # return False
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # O(1), O(1)
        if n>0 and n & (n-1) == 0:
            return True
        else:
            return False
        
        # O(logn), O(1)
        # if n == 1:
        #     return True

        # elif n%2 == 0:
        #     for i in range(31):
        #         if pow(2,i) == n:
        #             return True
        
        # return False
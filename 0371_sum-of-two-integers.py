class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0 and b!= 0:
            return b
        elif b == 0 and a != 0:
            return a
        
        return int( log2( 2**a * 2**b ) )
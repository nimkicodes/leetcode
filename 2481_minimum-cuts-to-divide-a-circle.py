class Solution:
    def numberOfCuts(self, n: int) -> int:
        return 0 if n == 1 else (n//2 if n%2 == 0 else n)

        # if n == 1:
        #     return 0
        
        # if n%2 == 0:
        #     return n//2
        
        # else:
        #     return n
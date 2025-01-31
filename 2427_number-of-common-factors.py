class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum((a % num == b % num == 0) for num in range(1, min(a,b)+1))
        
        # n = min(a,b) 
        # common_factor = 0
        # for num in range(1,n+1):
        #     if a % num == b % num == 0:
        #         common_factor += 1
        # return common_factor
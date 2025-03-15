class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]  
        seen = set(heap)  
        
        for _ in range(n):  
            ugly = heapq.heappop(heap)  
            
            for factor in [2, 3, 5]: 
                new_ugly = ugly * factor
                if new_ugly not in seen:
                    heapq.heappush(heap, new_ugly)
                    seen.add(new_ugly)
        
        return ugly  

        # this gave me TLE (time limit error) :( 
        # if n == 1:
        #     return 1 

        # def isUgly(n: int) -> int:
        #     for factor in [2,3,5]:
        #         while n % factor == 0:
        #             n //= factor 
        #     return n == 1

        # i, count = 2, 1
        # while True:
        #     if isUgly(i):
        #         count += 1
        #         if count == n:
        #             return i 
        #     i += 1
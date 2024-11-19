class Solution:
    def isHappy(self, n: int) -> bool:
        set_of_sums = set()

        while True:
            n = sum(map(lambda x: int(x)** 2, str(n)))
        
            if n == 1:
                return True
                
            elif n in set_of_sums:
                return False    
            
            set_of_sums.add(n)
class Solution:
    def powMultiplication(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n%2 == 0:
            y = self.powMultiplication(x, n/2)
            return y * y
        
        else:
            return x * self.powMultiplication(x, n-1)

    def myPow(self, x: float, n: int) -> float:   
        if n > 0:
            return self.powMultiplication(x,n)

        else:
            return 1/self.powMultiplication(x,-n)
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        remainder = 0
        while n>0:
            remainder = n%3
            if remainder == 2:
                return False
            n = n//3
        return True
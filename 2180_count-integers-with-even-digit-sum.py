class Solution:
    def countEven(self, num: int) -> int:
        def digitSum(n: int) -> int:
            return sum(int(digit) for digit in str(n))

        count = 0
        for n in range(1, num+1):
            if digitSum(n)%2 == 0:
                count += 1
        
        return count
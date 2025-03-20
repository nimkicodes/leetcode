class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digitSum(n: int) -> int:
            return sum(int(digit) for digit in str(n))
            
        return min(digitSum(n) for n in nums)
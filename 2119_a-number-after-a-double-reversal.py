class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        first_reverse = int(str(num)[::-1])
        second_reverse = int(str(first_reverse)[::-1])
        return True if second_reverse == num else False
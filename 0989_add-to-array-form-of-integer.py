import sys
sys.set_int_max_str_digits(10**6)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = int("".join(map(str, num)))
        return list(map(int, str(result + k)))
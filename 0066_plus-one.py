class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join((map(str, digits)))
        new_num = int(num) + 1
        plus_one = list(map(int, str(new_num)))
        
        return plus_one
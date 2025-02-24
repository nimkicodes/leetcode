class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        result = int(string[::-1]) if x >= 0 else -int(string[1:][::-1])
        return 0 if result < pow(-2,31) or result > pow(2,31)-1 else result
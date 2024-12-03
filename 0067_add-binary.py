class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_sum = int(a,2) + int(b,2)
        return bin(num_sum)[2:]
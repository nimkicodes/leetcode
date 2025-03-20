class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def getSum(s: str) -> int:
            converted = [ str(ord(char) - ord('a') + 1) for char in s ]
            num = "".join(converted)
            return sum(int(char) for char in num)

        result = getSum(s)
        for _ in range(k-1):
            result = sum(int(char) for char in str(result)) 
            if result < 10:
                break
        return result 
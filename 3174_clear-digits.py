class Solution:
    def clearDigits(self, s: str) -> str:
        result = []

        for char in s:
            if char.isdigit():
                result.pop()
            else:
                result.append(char)
    
        return "".join(result)
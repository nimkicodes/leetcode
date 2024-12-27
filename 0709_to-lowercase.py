class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        result = []
        for char in s:
            if char.isupper():
                result.append(chr(ord(char)+32))
            else:
                result.append(char)
        return "".join(result)
class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        result = ''
        for char in s:
            if ord(char) >= 65 and ord(char) <= 90:
                result += chr(ord(char)+32)
            else:
                result += char
        return result
class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ''.join(char.lower() for char in s if char.isalnum())

        for i in range(len(phrase) // 2):
            if phrase[i] != phrase[len(phrase) - i - 1]:
                return False
        return True
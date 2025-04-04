class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(":")", "{":"}", "[":"]"}

        # opening bracket char -> push to stack
        # closing bracket char -> pop from stack and check match with dictionary value
        
        for char in s:
            if char in d:
                stack.append(char)
            elif char in d.values():
                if len(stack) == 0 or d[stack.pop()] != char:
                    return False
        
        return len(stack) == 0
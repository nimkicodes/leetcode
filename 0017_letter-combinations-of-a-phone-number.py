class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        digit_to_letters = { "2": "abc",
                             "3": "def",
                             "4": "ghi",
                             "5": "jkl",
                             "6": "mno",
                             "7": "qprs",
                             "8": "tuv",
                             "9": "wxyz" 
                            }

        def backtrack(i, current_string):
            if len(current_string) == len(digits):
                result.append(current_string)
                return 
            
            for letter in digit_to_letters[digits[i]]:
                backtrack(i+1, current_string + letter)
            
        if digits:
            backtrack(0, "")
        
        return result
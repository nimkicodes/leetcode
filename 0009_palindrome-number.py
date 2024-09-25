class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        num = x
        if x>0:
            while num!=0:
                digit = num % 10
                reverse = (reverse * 10) + digit
                num = num // 10
            if reverse == x:
                return True
        elif x<0:
            return False
        else:
            return True
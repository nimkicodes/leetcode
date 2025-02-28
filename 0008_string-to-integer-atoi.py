class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        my_atoi = []

        for char in s:
            if (char == '+' or char == '-') and not my_atoi:
                my_atoi.append(char)
            elif char.isdigit():
                my_atoi.append(char)
            else:
                break

        if len(my_atoi) == 0 or my_atoi == ['+'] or my_atoi == ['-']:
            return 0

        result = "".join(my_atoi)
        int_MIN, int_MAX = -2**31, 2**31 - 1
        
        if int(result) < int_MIN:
            return int_MIN
        elif int(result) > int_MAX:
            return int_MAX
        else:
            return int(result)
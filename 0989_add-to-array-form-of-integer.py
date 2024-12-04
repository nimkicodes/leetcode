# import sys
# sys.set_int_max_str_digits(10**6)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # result = int("".join(map(str, num)))
        # return list(map(int, str(result + k)))
        
        int_k = list(map(int, str(k)))
        
        i, j = len(num) - 1, len(int_k) - 1
        carry = 0  
        result = []  

        while i >= 0 or j >= 0 or carry:
            
            x = num[i] if i >= 0 else 0
            y = int_k[j] if j >= 0 else 0
            
            total = x + y + carry
            carry = total // 10 
            result.append(total % 10)  

            i -= 1
            j -= 1

        return result[::-1]
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def divideString(s: str, k: int) -> List[str]: 
            return [s[i:i+k] for i in range(0, len(s), k)] 

        while k < len(s):  
            groups = divideString(s, k)
            group_sum = [str(sum(int(digit) for digit in group)) for group in groups]  
            s = "".join(group_sum) 

        return s
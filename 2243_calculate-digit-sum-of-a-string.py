class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def divideString(s: str, k: int) -> List[str]: 
            l, n = [], len(s)
            for i in range(0, n, k):
                l.append(s[i:min(i + k, n)])
            return l
        
        while len(s)>k: 
            arr, temp = divideString(s, k), [] 
            for group in arr: 
                group_sum = 0
                for digit in group:
                    group_sum += int(digit)
                temp.append(str(group_sum)) 
            s = ''.join(temp) 
        return s
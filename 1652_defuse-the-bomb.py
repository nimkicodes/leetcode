class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = len(code)
        defused_bomb = []
        
        if k == 0:
            for i in range(l):    
                code[i] = 0
            return code
        
        if k > 0:
            for i in range(l):
                temp = 0
                for j in range(1, k+1):
                    temp = temp + code[(i+j)%l]
                defused_bomb.append(temp)
            return defused_bomb
        
        if k < 0:
            for i in range(l):
                temp = 0
                for j in range(1, abs(k)+1):
                    temp = temp + code[(i-j)%l]
                defused_bomb.append(temp)
            return defused_bomb
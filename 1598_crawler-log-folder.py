class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step = 0
        
        for log in logs: 
            if log == "../":
                step -= 1 if step > 0 else 0
            elif log == "./":
                continue
            else:
                step += 1
        
        return step
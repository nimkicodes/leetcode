class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            if (int(details[i][11])*10 + int(details[i][12])) > 60:
                count += 1
        
        return count
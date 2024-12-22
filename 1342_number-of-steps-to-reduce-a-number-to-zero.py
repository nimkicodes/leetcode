class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            steps += 1
        
        return steps
        
        # recursion, because it's fun
        # if num == 0:
        #     return 0

        # if num % 2 == 0:
        #     return self.numberOfSteps(num / 2) + 1
        
        # return self.numberOfSteps(num - 1) + 1

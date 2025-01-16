class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        
        equal_sum = sum(arr) // 3
        check_sum, partition = 0, 0
        
        for num in arr:
            check_sum += num
            
            if check_sum == equal_sum:
                check_sum = 0
                partition += 1
            
            if partition == 3:
                return True

        return False
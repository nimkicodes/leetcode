class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        window_end, farthest = 0, 0
        best_index = 0

        for i in range(len(nums) - 1):  
            if i + nums[i] > farthest:
                farthest = i + nums[i]
                best_index = i

            if i == window_end:
                jumps += 1
                print("jump"+ str(jumps) + " : jump from " + str(best_index))
                window_end = farthest
        
        return jumps
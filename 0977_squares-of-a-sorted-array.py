class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # bruteforce, O(n log n)
        nums.sort(key=abs)
        sorted_squares = []
        
        for i in range(len(nums)):
            sorted_squares.append(nums[i]*nums[i])
        
        return sorted_squares
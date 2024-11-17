class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # two pointers, O(n)
        left, right = 0, len(nums)-1
        index = len(nums)-1
        sorted_squares = [0] * len(nums)
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                sorted_squares[index] = pow(nums[left], 2)
                left += 1
            else:
                sorted_squares[index] = pow(nums[right], 2)
                right -= 1
            index -= 1
        
        return sorted_squares

        # bruteforce, O(n log n)
        # nums.sort(key=abs)
        # sorted_squares = []
        
        # for i in range(len(nums)):
        #     sorted_squares.append(nums[i]*nums[i])
        
        # return sorted_squares
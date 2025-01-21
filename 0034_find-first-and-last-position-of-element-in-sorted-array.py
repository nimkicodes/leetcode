class Solution:
    def doBinarySearch(self, nums: List[int], target: int, is_searching_left: bool) -> int:
        left, right, index = 0, len(nums)-1, -1
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] > target: 
                right = middle - 1

            elif nums[middle] < target: 
                left = middle + 1
            
            else:
                index = middle 
                
                if is_searching_left:
                    right = middle - 1
                else:
                    left = middle + 1

        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.doBinarySearch(nums, target, True)
        right = self.doBinarySearch(nums, target, False)
        return [left, right]
        
    # video solution by CodingNinja (review): https://www.youtube.com/watch?v=441pamgku74
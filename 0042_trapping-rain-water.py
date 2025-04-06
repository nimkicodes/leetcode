class Solution:
    def trap(self, height: List[int]) -> int:
        # O(1) time, O(n) space
        n, water = len(height), 0
        left, right = [0]*n , [0]*n
        left[0], right[n-1] = height[0], height[n-1]

        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        for i in range(n-2, 0, -1):
            right[i] = max(right[i+1], height[i])

        for i in range(n):
            h = min(left[i], right[i])     
            water += max(0, h - height[i])

        return water
        
        # two pointers, O(n) time, O(1) space
        # left , right = 0, len(height)-1
        # max_left, max_right = height[left], height[right]
        # water = 0

        # while left < right:
        #     if max_left < max_right:
        #         left += 1
        #         max_left = max(max_left, height[left])
        #         water += max(0, max_left - height[left])
        #     else:
        #         right -= 1
        #         max_right = max(max_right, height[right])
        #         water += max(0, max_right - height[right])

        # return water
        
        # bruteforce, O(n2) time, space O(1)
        # water = 0
        
        # for i in range(1, len(height)-1):
        #     max_left = max(height[:i])
        #     max_right = max(height[i+1:])

        #     min_height = min(max_left, max_right)

        #     if min_height > height[i]:
        #         water += min_height - height[i]
            
        # return water 
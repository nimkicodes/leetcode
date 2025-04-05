class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers, O(n)
        left , right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        water = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                water += max(0, max_left - height[left])
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water += max(0, max_right - height[right])

        return water
        
        # bruteforce, O(n2)
        # water = 0
        
        # for i in range(1, len(height)-1):
        #     max_left = max(height[:i])
        #     max_right = max(height[i+1:])

        #     min_height = min(max_left, max_right)

        #     if min_height > height[i]:
        #         water += min_height - height[i]
            
        # return water 
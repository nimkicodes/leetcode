class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map = {}
        stack = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                popped_element = stack.pop()
                next_greater_map[popped_element] = num
            
            stack.append(num)
            
        result = [next_greater_map.get(num, -1) for num in nums1]
        return result
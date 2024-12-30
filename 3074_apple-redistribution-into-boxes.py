class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total_apples = sum(apple)
        total_capacity, box_count = 0, 0
        
        for box in capacity:
            total_capacity += box
            box_count += 1
            if total_capacity >= total_apples:
                return box_count
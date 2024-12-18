class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_type = defaultdict(int)
        
        for variety in candyType:
            candy_type[variety] += 1
        
        return min(len(candyType)//2, len(candy_type))
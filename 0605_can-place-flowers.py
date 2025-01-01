class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, plot in enumerate(flowerbed):
            left = 0 if i == 0 else flowerbed[i-1]
            right = 0 if i == len(flowerbed) - 1 else flowerbed[i+1]

            if n > 0 and left == 0 and right == 0 and plot == 0:
                n -= 1
                flowerbed[i] = 1
        
        return n == 0
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set(jewels)
        stone = Counter(stones)
        
        result = 0
        for j in jewels:
            result += stone[j]
        return result
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = Counter(char.lower() for char in licensePlate if char.isalpha())
        shortest = None

        for word in words:
            if not shortest or len(word) < len(shortest):
                word_count = Counter(word)
                if all(word_count[char] >= required for char, required in plate.items()):
                    shortest = word
        
        return shortest
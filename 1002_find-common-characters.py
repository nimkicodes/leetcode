class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        first = set(words[0])
        
        for char in first:
            count = min([word.count(char) for word in words])
            if count > 0:
                result += [char] * count
        return result
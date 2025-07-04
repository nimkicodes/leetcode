class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def mapping(words):
            mapping = {}
            code = []

            for i, char in enumerate(words):
                if char not in mapping:
                    mapping[char] = len(mapping)
                code.append(mapping[char])
            
            return code
        
        pattern_code = mapping(pattern)
        result = []

        for word in words:
            if mapping(word) == pattern_code:
                result.append(word)

        return result
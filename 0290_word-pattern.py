class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, mapping = s.split(' '), dict()

        if len(set(pattern)) != len(set(words)):
            return False

        for i in range(len(words)):
            if words[i] not in mapping:
                mapping[words[i]] = pattern[i]
            elif mapping[words[i]] != pattern[i]:
                return False
    
        return True
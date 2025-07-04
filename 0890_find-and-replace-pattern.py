class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matching(word, pattern):
            if len(word) != len(pattern):
                return False

            w_map, p_map = {}, {}

            for w, p in zip(word, pattern):
                if w not in w_map:
                    w_map[w] = p
                elif w_map[w] != p:
                    return False

                if p not in p_map:
                    p_map[p] = w
                elif p_map[p] != w:
                    return False

            return True

        return [word for word in words if matching(word, pattern)]
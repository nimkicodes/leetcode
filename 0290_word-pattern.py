class Solution:
    def wordPattern(self, pattern, s):
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

        return matching(s.split(), pattern)
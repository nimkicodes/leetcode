class Solution:
    def countPoints(self, rings: str) -> int:
        dict_rings = defaultdict(set)

        for i in range(1, len(rings)+1, 2):
            rod, color = rings[i], rings[i-1]
            dict_rings[rod].add(color)

        return sum(1 for rod, color in dict_rings.items() if len(color) == 3)

        # dict_rings = {}
        # for i in range(1, len(rings)+1, 2):
        #     if rings[i] in dict_rings:
        #         dict_rings[rings[i]].add(rings[i-1])
        #     else:
        #         dict_rings[rings[i]] = set(rings[i-1])
        
        # result = 0
        # for rod, color in dict_rings.items():
        #     if len(color) == 3:
        #         result += 1
        # return result
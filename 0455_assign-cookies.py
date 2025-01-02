class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        greed, cookie_size, contented_kids = 0, 0, 0

        for cookie_size in s:
            if cookie_size >= g[greed]:
                contented_kids += 1
                greed += 1
                
            if greed >= len(g):
                break

        return contented_kids
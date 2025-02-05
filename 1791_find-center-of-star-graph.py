class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # time: O(1)
        a, b = edges[0]
        if edges[1][0] == a or edges[1][1] == a:
            return a
        return b
        
        # edge_set = [set(edge) for edge in edges]
        # star = {}
        # for i in range(len(edge_set)-1):
        #     star = edge_set[i] & edge_set[i-1]
        # return star.pop()
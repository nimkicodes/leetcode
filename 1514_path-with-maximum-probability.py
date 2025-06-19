class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            adj[u].append( [ v, succProb[i] ] )
            adj[v].append( [ u, succProb[i] ] )

        pq = [ (-1, start_node) ]        # python only supports min heap, we need max heap
        visit = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)

            if cur == end_node:
                return prob * -1

            for neighbour, edgeProb in adj[cur]:
                if neighbour not in visit:
                    heapq.heappush( pq, (prob * edgeProb, neighbour) )
        return 0
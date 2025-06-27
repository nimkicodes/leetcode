class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        def dfs(current):
            if current == destination:
                return True
            
            if visited[current]:
                return False 
            visited[current] = True

            for neighbour in adj[current]:
                if dfs(neighbour):
                    return True
            return False 

        return dfs(source)
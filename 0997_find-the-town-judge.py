class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        in_degree = [0] * (n+1)
        out_degree = [0] * (n+1)

        for u, v in trust: 
            out_degree[u] += 1
            in_degree[v] += 1

        for i in range(1, n+1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i

        return -1
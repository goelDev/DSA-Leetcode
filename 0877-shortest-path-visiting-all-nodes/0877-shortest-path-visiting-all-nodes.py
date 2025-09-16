class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        memo = {}
    
        def backtrack(i: int, visited: frozenset) -> int:
            key = (i, visited)
            if len(visited.union([i])) == N:
                return 0

            if key in memo:
                return memo[key]

            memo[key] = float('inf')
            
            for nbr in graph[i]:
                if nbr in visited:
                    continue
                memo[key] = min(memo[key], 1 + backtrack(nbr, visited))
    
                memo[key] = min(memo[key], 1 + backtrack(nbr, visited.union([i])))

            return memo[key]
        
        return min(backtrack(i, frozenset()) for i in range(N))
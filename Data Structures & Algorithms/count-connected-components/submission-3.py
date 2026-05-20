class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        deps = [[] for _ in range(n)]
        parent = [i for i in range(n)]

        for a, b in edges:
            deps[a].append(b)
            deps[b].append(a)

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        graphs = n

        def union(a, b):
            is_union = find(a) != find(b)
            if is_union:
                parent[find(b)] = find(a)
            return is_union
        
        for a in range(n):
            for b in deps[a]:
                if union(a, b):
                    graphs -=1
        
        return graphs

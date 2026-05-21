class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges))]
        rank = [1] * len(edges)

        def find(n):
            while parents[n] != n:
                parents[n] = parents[parents[n]]
                n = parents[n]
            return parents[n]

        def union(a, b):
            afind = find(a)
            bfind = find(b)
            if afind == bfind:
                return True

            if rank[afind] < rank[bfind]:
                afind, bfind = bfind, afind
            rank[afind] += rank[bfind]
            parents[bfind] = afind 
            return False
        
        for a, b in edges:
            if union(a-1, b-1):
                return [a, b]
        return []
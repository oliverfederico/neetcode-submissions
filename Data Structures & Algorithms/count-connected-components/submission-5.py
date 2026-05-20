class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = [i for i in range(n)]
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            
            if root_a != root_b:
                parent[root_b] = root_a
                return True
            return False
            
        graphs = n
        
        # Iterate over the given edges directly
        for a, b in edges:
            if union(a, b):
                graphs -= 1
                
        return graphs
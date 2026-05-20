class Solution:
    # a valid tree has no cycles and there cam only be 1 tree, not multiple
    # find the root of the tree or find the leaves
    # leaves only have 1 dep
    # remove all leave repeatedly until we remove all nodes or run out of leaves, i.e there is a cycle
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        connections = [0] * n
        cmap = [set() for _ in range(n)]
        for a, b in edges:
            cmap[a].add(b)
            connections[a] +=1
            cmap[b].add(a)
            connections[b] +=1
        
        q = deque()

        for node in range(n):
            if connections[node] == 1:
                q.append(node)
        
        validated = 0

        while q:
            node = q.popleft()
            validated += 1
            for c in cmap[node]:
                connections[c] -= 1
                cmap[c].remove(node)
                if connections[c] == 0 and validated < n-1:
                    return False
                if connections[c] == 1:
                    q.append(c)
        
        return validated == n
             
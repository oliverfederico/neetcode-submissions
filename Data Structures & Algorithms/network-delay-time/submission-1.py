class Solution: 
    # we always want to process the cheapest path + edge next
    # does it matter if we take the cheapest node + path or just the cheapest path of currently cheapest node
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        deps = [[] for _ in range(n+1)]
        for u, v, t in times:
            deps[u].append((t, v))

        mheap = deps[k].copy()
        heapq.heapify(mheap)
        visited = set([k])

        while mheap:
            c, u = heapq.heappop(mheap)
            if u not in visited:
                visited.add(u)
                if len(visited) == n:
                            return c
                for t, v in deps[u]:
                    if v not in visited:
                        heapq.heappush(mheap, (c+t, v))
                        
        
        return -1
            
        
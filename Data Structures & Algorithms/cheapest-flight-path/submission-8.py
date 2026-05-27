from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append((v, cst))

        q = deque([(0, src, 0)])
        
        while q:
            cst, node, stops = q.popleft()

            for nei, w in adj[node]:
                nextCost = cst + w
                
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    
                    # Your optimization: Only enqueue if we haven't exhausted our stops.
                    # We also keep the 'nei != dst' optimization from earlier.
                    if stops < k and nei != dst:
                        q.append((nextCost, nei, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1
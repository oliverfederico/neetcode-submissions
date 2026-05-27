class Solution:
    # we should greedily choose the cheapest flight, 
    # if stops = k-1 then we either can fly to dst or we step back until we find dst or a more direct route
    # dijstra? 
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for a, b, p in flights:
            adj[a].append((p, b))
        mheap = [(0, 0, src)]
        
        while mheap:
            total, stops, curr = heapq.heappop(mheap)

            if curr == dst:
                return total

            for cost, cand in adj[curr]:
                if stops <= k:
                    heapq.heappush(mheap, (total + cost, stops + 1, cand))


        return -1
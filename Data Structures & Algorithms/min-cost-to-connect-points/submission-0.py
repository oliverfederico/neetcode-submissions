class Solution:
    # sort on (x + y)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost = 0
        num_points = len(points)
        costs = [[0]*num_points for _ in range(num_points)]

        for i in range(num_points):
            for j in range(num_points):
                for p in range(2): 
                    costs[i][j] += abs(points[i][p]- points[j][p])
        
        mheap = [(0,0)]
        visited = set()

        while mheap:
            c, i = heapq.heappop(mheap)
            if i in visited:
                continue
            min_cost += c
            visited.add(i)

            if len(visited) == num_points:
                return min_cost
            
            for j in range(num_points):
                if j != i:
                    heapq.heappush(mheap, (costs[i][j],j))

        


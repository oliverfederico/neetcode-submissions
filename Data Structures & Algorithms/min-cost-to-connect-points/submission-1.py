class Solution:
    # sort on (x + y)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost = 0
        num_points = len(points)
        
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
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(mheap, (dist, j))

        


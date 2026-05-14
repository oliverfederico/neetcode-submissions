class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        q = deque()

        def bfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            q.append((r-1,c))
            q.append((r+1,c))
            q.append((r,c-1))
            q.append((r,c+1))
            grid[r][c] = 0
            area = 1
            for _ in range(4):
                nr, nc = q.popleft()
                area += bfs(nr, nc)
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r,c))
        
        return max_area
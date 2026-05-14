class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            area = 0
            while q:
                row, col = q.popleft()
                area+=1
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 0
       
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r,c))
        
        return max_area
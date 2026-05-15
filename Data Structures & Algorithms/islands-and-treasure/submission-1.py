class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c, 0))
        
        while q:
            row, col, distance = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    grid[nr][nc] = distance + 1
                    q.append((nr, nc, distance + 1))


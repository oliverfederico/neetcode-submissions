class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        ROWS, COLS = len(grid), len(grid[0])
        minute = 0

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        q.append((-1,-1))

        while q:
            row, col = q.popleft()
            if row == -1 and q:
                minute += 1
                q.append((-1,-1))
            else:
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return minute


        
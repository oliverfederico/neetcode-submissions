class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        ROWS, COLS = len(grid), len(grid[0])
        minute = 0
        fresh_oranges = 0

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0
        
        while q and fresh_oranges > 0:
            minute += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        q.append((nr,nc))
        
        return minute if fresh_oranges == 0 else -1


        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            board[r][c] = 'I'
            surrounded = True
            
            while q and surrounded:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 < nr < ROWS - 1 and 0 < nc < COLS - 1:
                        if board[nr][nc] == 'O':
                            board[nr][nc] = 'I'
                            q.append((nr,nc))
                    elif board[nr][nc] == 'O':
                        surrounded = False
                        q.clear()
                        break
            
            q.append((r,c))
            val = 'X' if surrounded else 'O'
            board[r][c] = val
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 < nr < ROWS - 1 and 0 < nc < COLS - 1 and board[nr][nc] == 'I':
                            board[nr][nc] = val
                            q.append((nr,nc))

        for r in range(1,ROWS-1):
            for c in range(1,COLS-1):
                if board[r][c] == 'O':
                    bfs(r, c)

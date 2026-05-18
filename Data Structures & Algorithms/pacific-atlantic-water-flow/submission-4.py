from _heapq import heapify
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        flows = [[None for _ in range(COLS)] for _ in range(ROWS)]
        result = []

        def dfs(r, c):
            pacific = r == 0 or c == 0
            atlantic = r == ROWS -1 or c == COLS - 1
            flows[r][c] = (pacific, atlantic)
            downs = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] <= heights[r][c]:
                    downs.append((nr, nc))
            downs.sort(key=lambda x: heights[x[0]][x[1]])
            for nr, nc in downs:
                if not flows[nr][nc]:
                    if heights[nr][nc] < heights[r][c]:
                        dfs(nr, nc)
                    else:
                        heights[r][c] -= 1
                        dfs(nr, nc)
                        heights[r][c] += 1
                np, na = flows[nr][nc]
                pacific |= np
                atlantic |= na
                flows[r][c] = (pacific, atlantic)
            if pacific and atlantic:
                result.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if not flows[r][c]:
                    dfs(r, c) 

        return result
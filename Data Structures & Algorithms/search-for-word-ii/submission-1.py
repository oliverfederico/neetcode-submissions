class Solution:
    # most bf - for each word, traverse whole board, dfs/bfs on potentials - worst case O(w*(m*n)^2)
    # build trie/board map, traverse
    # we want to store every substring of words and try to start at the longest substring of a given word we find?
    # we are a graph with a-z as nodes and connections built the string
    #
    # for each position we want all the substrings that can be found from it, 
    # we then select the longest substring that is a substring of our current word
    # or
    # for each substring we find, we store the list of co-ords that create it,
    # we then select 


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        DIRS = [(0,-1), (0,1), (-1,0), (1,0)]
        ROWS, COLS = len(board), len(board[0])
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['*'] = {}
        found = []
        
        def dfs(r, c, curr_level, word, visited):
            if '*' in curr_level:
                found.append(''.join(word))
                curr_level.pop('*')
            if not(0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited) or board[r][c] not in curr_level:
                return False
            word.append(board[r][c])
            visited.add((r,c))
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, curr_level[board[r][c]], word, visited)
            word.pop()
            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, [], set())

               

    
        return found
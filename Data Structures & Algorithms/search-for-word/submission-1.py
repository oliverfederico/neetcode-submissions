class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def search(char_idx, i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] != word[char_idx]:
                return False
            if char_idx == len(word) - 1:
                return True
            board[i][j] = ""

            found = (search(char_idx+1, i-1, j) or
                     search(char_idx+1, i+1, j) or
                     search(char_idx+1, i, j-1) or
                     search(char_idx+1, i, j+1))
            
            board[i][j] = word[char_idx]
            return found
        
        for i in range(ROWS):
            for j in range(COLS):
                if search(0, i, j):
                    return True
                    
        return False
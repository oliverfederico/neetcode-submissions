class Solution:
    # iterate till we find first letter, then look for adjacent second letter and repeat.
    # Set letter to "" to avoid repeat searching - we can't do this as the same letter might be used again elsewhere
    # we need to backtrack to take other paths if multiple adjacent choices 
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(char_idx, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[char_idx]:
                return False
            if char_idx == len(word) - 1:
                return True
            board[i][j] = ""

            found = False
            if search(char_idx+1, i-1, j):
                found = True
            elif search(char_idx+1, i+1, j):
                found = True
            elif search(char_idx+1, i, j-1):
                found = True
            elif search(char_idx+1, i, j+1):
                found = True
            
            board[i][j] = word[char_idx]
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(0, i, j):
                    return True
                    
        return False

        
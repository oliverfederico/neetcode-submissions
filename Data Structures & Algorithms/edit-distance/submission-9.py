class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
            
        m, n = len(word1), len(word2)
        
        # 1. Allocate BOTH arrays strictly once
        prev_row = [j for j in range(n + 1)]
        curr_row = [0] * (n + 1)
        
        for i in range(1, m + 1):
            # 2. Overwrite the base case for the current row
            curr_row[0] = i
            
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr_row[j] = prev_row[j - 1]
                else:
                    curr_row[j] = min(
                        curr_row[j - 1], # Insert
                        prev_row[j],     # Delete
                        prev_row[j - 1]  # Replace
                    ) + 1
            
            # 3. Swap the pointers! 
            # The newly calculated curr_row becomes the prev_row for the next loop.
            # The old prev_row becomes the curr_row, which will simply be overwritten.
            prev_row, curr_row = curr_row, prev_row
            
        # 4. Because we swap at the very end of the loop, the final computed 
        # row actually lives in prev_row right now!
        return prev_row[n]
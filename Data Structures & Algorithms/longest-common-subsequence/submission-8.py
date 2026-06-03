class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Optimization: make text2 the shorter string for space efficiency
        if len(text2) > len(text1):
            text1, text2 = text2, text1
            
        # Two 1D arrays
        prev_row = [0] * (len(text2) + 1)
        curr_row = [0] * (len(text2) + 1)
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    # Diagonal + 1 (from the previous row)
                    curr_row[j+1] = prev_row[j] + 1
                else:
                    # Max of Left (current row) or Top (previous row)
                    curr_row[j+1] = max(curr_row[j], prev_row[j+1])
            
            # Swap pointers for the next iteration
            prev_row, curr_row = curr_row, prev_row
            
        # Because we swapped at the very end of the loop, 
        # the final result is now sitting in prev_row!
        return prev_row[-1]
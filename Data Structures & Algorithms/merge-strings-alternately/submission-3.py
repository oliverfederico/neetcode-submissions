class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        # Calculate lengths and the minimum bound exactly once
        n, m = len(word1), len(word2)
        min_len = min(n, m)
        
        # Loop strictly for the overlap (no 'if' checks needed)
        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])
            
        # Append the remaining slices (slicing in Python is fast!)
        # If min_len == n, word1[min_len:] is just an empty string, which is harmless.
        merged.append(word1[min_len:])
        merged.append(word2[min_len:])
        
        return "".join(merged)
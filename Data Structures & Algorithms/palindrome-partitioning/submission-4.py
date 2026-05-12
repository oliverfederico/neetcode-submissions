class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res, part = [], []
        
        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                # Check palindrome on the fly using Python slicing
                sub = s[i : j + 1]
                if sub == sub[::-1]:
                    part.append(sub)
                    dfs(j + 1)
                    part.pop()
                    
        dfs(0)
        return res
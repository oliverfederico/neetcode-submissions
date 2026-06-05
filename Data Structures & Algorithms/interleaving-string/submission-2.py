class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2)+1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(0, len(s3)):
            for j in range(i+1):
                if i-j <= len(s1) and j <= len(s2):
                    if dp[i-j][j]:
                        if i-j < len(s1):
                            dp[i-j+1][j] |= s1[i-j] == s3[i]
                        if j < len(s2):
                            dp[i-j][j+1] |= s2[j] == s3[i]
        return dp[-1][-1]
                    

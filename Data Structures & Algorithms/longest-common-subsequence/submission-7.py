class Solution:
    # assume len text1 >= len text2 wlog then text1 contains subsequence in text2
    # fo
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
               
        return dp[-1][-1]
        


            

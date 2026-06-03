class Solution:
    # assume len text1 >= len text2 wlog then text1 contains subsequence in text2
    # fo
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dp = [0] * (len(text2) + 1)
        
        for i in range(len(text1)):
            prev = 0
            for j in range(len(text2)):
                temp = dp[j+1]
                if text1[i] == text2[j]:
                    dp[j+1] = prev + 1
                else:
                    dp[j+1] = max(dp[j+1], dp[j])
                prev = temp
               
        return dp[-1]
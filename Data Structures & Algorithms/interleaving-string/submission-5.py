class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        dp = [False] * (len(s2)+1)
        dp[0] = True
        nextDp = True

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                res = False if j > 0 else nextDp
                res |= (0 < i and dp[j] and s1[i-1] == s3[i+j-1]) or (0 < j and nextDp and s2[j-1] == s3[i+j-1])
                dp[j] = res
                nextDp = dp[j]
            nextDp = False
            print(dp)
            print('---')
        print('------')
        print(dp)
        return dp[-1]
                    

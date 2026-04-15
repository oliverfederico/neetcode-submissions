class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in range(len(strs[0])):
            for s in strs:
                if len(s) == i or strs[0][i] != s[i]:
                    return lcp
            lcp += strs[0][i]
        return lcp    
                
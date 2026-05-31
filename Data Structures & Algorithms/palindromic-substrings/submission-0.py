class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):

            j, k = i, i
            while 0 <= j and k < len(s) and s[j]==s[k]:
                j-=1
                k+=1
                count +=1
            
            j, k = i, i+1
            while 0 <= j and k < len(s) and s[j]==s[k]:
                j-=1
                k+=1
                count +=1
        return count
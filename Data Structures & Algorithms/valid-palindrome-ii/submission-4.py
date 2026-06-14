class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1
        while l < r:
            if s[l] != s[r]:
                print(s[l], s[r])
                if l + r != n-1:
                    return False
                if l == r-1:
                    return True
                if s[l+1] == s[r] and s[l+2] == s[r-1]:
                    l+=1
                elif s[r-1] == s[l] and s[l+1] == s[r-2]:
                    r-=1
                else:
                    return False
            l+=1
            r-=1
        return True
class Solution:
    # every letter is a palindrome
    # brute force would be to check all substrings so 2^n?
    # reverse s, traverse s', we are looking for the longest sequence where the letters line up
    # i.e the longest common substring, 
    # partition at each index, 
    # are both s and s' equal, then we remove a letter from each side
    # "abbacfbba"
    # "ababd" "dbaba" -> "abab" + "baba" and "babd" + "dbab"
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = (1,0)
        q = [(i,i) for i in range(len(s))]
        for i in range(len(s)-1):
            q.append((i,i+1))
        while q:
            l, r = q.pop()
            if 0 <= l and r < len(s) and s[l] == s[r]:
                q.append((l-1, r+1))
                if longest[1]-longest[0] < r-l:
                    longest = (l,r)
        return s[longest[0]:longest[1]+1]
            
            




        # s_p = list(reversed(s))
        # chars = defaultdict(list)
        # # for i in range(len(s)):
        # #     chars[s[i]].append(i)
        # # for i in range(len(s)):
        # #     s[i] 
        # for i in range(len(s)):
        #     j = 0
        #     while 0 <= i-j and i+j < len(s) and s[i-j]== s[i+j]:
        #         j+=1
        #     if 
                
            
        
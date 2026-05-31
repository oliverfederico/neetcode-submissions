class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        curr, prev, prevprev = 1, 0, 0
        grouped = False
        for i in range(len(s)-1):         
            if (s[i] == '1' or s[i] == '2'):
                if (s[i] == '2' and s[i+1] != '7' and s[i+1] != '8' and s[i+1] != '9' or s[i] == '1') and s[i+1] != '0':
                    if i + 2 < len(s) and s[i+2] == '0':
                        grouped = False
                        continue
                    temp = curr
                    if grouped:
                        curr += prev
                    else:
                        curr *= 2
                    print(curr)
                    prev = temp
                    grouped = True
                    continue
            elif s[i+1] == '0':
                return 0
            grouped = False
            
        return curr
        

class Solution:
    # ((*())
    def checkValidString(self, s: str) -> bool:
        lefts = rights = stars = rstars = 0
        for c in s:
            if c == '(':
                lefts += 1
                stars = 0
            elif c == ')':
                if lefts:
                    lefts -= 1
                elif rstars:
                    stars += 1
                    rstars -= 1
                elif stars:
                    stars -= 1
                else:
                    return False
            elif c == '*':
                if lefts:
                    lefts -= 1
                    rstars += 1
                else:
                    stars += 1
                
        return lefts <= stars
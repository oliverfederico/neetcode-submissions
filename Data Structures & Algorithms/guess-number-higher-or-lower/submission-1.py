# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n + 1
        g = (l+r)//2
        res = guess(g)
        while res:
            if res < 0:
                r = g
            else:
                l = g
            g = (l + r)//2
            res = guess(g)
        return g
        
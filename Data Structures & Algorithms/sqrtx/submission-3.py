class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        r = x // 2
        while r * r > x:
            r = (r + x // r) >> 1
        return r
class Solution:
    # 1001 | 0011-> 100
    # for large x, sqrt will be in the 
    def mySqrt(self, x: int) -> int:
        sqrt = 1
        while sqrt * sqrt < x:
            sqrt = sqrt << 1
        print(sqrt)
        l = sqrt >> 1
        r = sqrt
        m = (l+r)//2
        while l <= r:
            sqr = m * m
            if sqr == x:
                return m
            if sqr < x:
                l = m + 1
            else:
                r = m - 1
            m = (l+r)//2
        return r


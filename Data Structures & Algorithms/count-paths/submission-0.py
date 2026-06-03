class Solution:
    # 1, 0 -> 1,
    # 0, 1 -> 1,
    #         20 10  4  1
    # 21, 15, 10, 6, 3, 1
    #  6,  5,  4, 3, 2, 1
    #  1,  1,  1, 1, 1, 1
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m+n-2)//(math.factorial(n-1)*math.factorial(m-1))

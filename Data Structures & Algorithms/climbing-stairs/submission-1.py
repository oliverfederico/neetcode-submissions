class Solution:
    def climbStairs(self, n: int) -> int:
        grandchild = 1
        child = 1
        for _ in range(n - 1):
            grandchild, child = child, child + grandchild
        return child
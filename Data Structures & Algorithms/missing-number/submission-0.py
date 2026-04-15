class Solution:
    # 000 001 010 011 -> 100 | 1 10 11 100 -> 
    # 01 10 11 -> 00
    # 00 01 10 -> 11 | 01 10 11 -> 0 ^ 11 -> 11
    # 00 10 -> 01
    # 00 01 -> 10 
    # n*n+1/2
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return ((n*(n+1))//2) - sum(nums)
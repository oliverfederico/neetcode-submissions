class Solution:
    # 2^a * 2^b = 2^a+b
    # a * 2^b
    def getSum(self, a: int, b: int) -> int:
# 32-bit bitmask to simulate standard integer overflow
        mask = 0xFFFFFFFF
        
        while b != 0:
            # a ^ b is the sum without carry
            # (a & b) << 1 is the carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # In 32-bit systems, if the 32nd bit is 1, the number is negative.
        max_int = 0x7FFFFFFF
        return a if a <= max_int else ~(a ^ mask)
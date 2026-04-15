class Solution:
    def reverseBits(self, n: int) -> int:
        flipped = 0
        for i in range(31):
            flipped |= (n & 1)
            flipped <<= 1
            n >>= 1
        return flipped | n
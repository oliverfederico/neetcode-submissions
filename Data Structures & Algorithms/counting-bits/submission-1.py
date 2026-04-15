class Solution:
    # 5-> 101, 6-> 110, 7-> 111, 8->1000 
    def countBits(self, n: int) -> List[int]:
        output = [0]
        for i in range(1, n+1):
            output.append(output[i//2] + (1 if i % 2 != 0 else 0))
        return output
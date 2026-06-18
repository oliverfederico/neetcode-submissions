class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        curr = []
        for num in nums:
            n = len(curr)
            for i in range(n):
                curr.append(curr[i] ^ num)
                total += curr[-1]
            curr.append(num)
            total += num
            print(total)
        return total
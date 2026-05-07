class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(comb, subset, value):
            if value == target:
                result.append(comb.copy())
            if value > target:
                return 

            for i in range(len(subset)):
                comb.append(subset[i])
                dfs(comb, subset[i:], value+subset[i])
                comb.pop()


        dfs([], nums, 0)
        return result
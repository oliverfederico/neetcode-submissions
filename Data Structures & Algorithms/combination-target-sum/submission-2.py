class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(comb, i, value):
            if value == target:
                result.append(comb.copy())
                return

            for j in range(i, len(nums)):
                if value + nums[j] > target:
                    return 
                comb.append(nums[j])
                dfs(comb, j, value+nums[j])
                comb.pop()


        dfs([], 0, 0)
        return result
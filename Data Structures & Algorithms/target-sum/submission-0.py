class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # total = sum(nums)
        # dp = [0] * (total + 1)
        # dp[nums[0]] = 1
        # for num in nums[1:]:
        #     for j in range(total + 1):
        #         if dp[j]:
        #             dp[abs(j-num)] += 1
        #             dp[abs(j+num)] += 1
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == 0 else 0
            return dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
        return dfs(0, target)
                    
                    
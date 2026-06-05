class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # If target is impossible to reach, or if the subset sum isn't an integer
        if abs(target) > total or (target + total) % 2 != 0:
            return 0
            
        subset_sum = (target + total) // 2
        
        # dp[i] represents the number of ways to reach sum i
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # 1 way to reach sum 0 (choose no elements)
        
        for num in nums:
            # Iterate backwards to avoid reusing the same number in the same step
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_sum]
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
        dp = defaultdict(int)
        dp[nums[0]] += 2
        for num in nums[1:]:
            temp = defaultdict(int)
            for k, v in dp.items():
                temp[k+num] += v
                temp[abs(k-num)] += v
            dp = temp
            print(dp)
        if target < 0:
            target *= -1
        if target == 0 and 0 in dp:
            return dp[0] 
        return (dp[target]+1)//2 if target in dp else 0

        
        # def dfs(i, total):
        #     if i == len(nums):
        #         return 1 if total == 0 else 0
        #     return dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
        # return dfs(0, target)
                    
                    
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
        dp[0] = 1
        for num in nums:
            temp = defaultdict(int)
            for k, v in dp.items():
                temp[k+num] += v
                temp[k-num] += v
            dp = temp
            print(dp)
        return dp[target]
        
                    
                    
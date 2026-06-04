class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [0] * (amount + 1)
        # for c in coins:
        #     dp[c][c] = 1
        # for c in coins:
        #     dp[c] = 1
        for c in coins:
            dp[c] += 1
            for i in range(1, amount+1-c):
                dp[i+c]+= dp[i]
            # print(dp)
            
        return dp[-1]

        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = [0] * len(prices)
        buy = [0] * len(prices)
        buy[0] = -prices[0]


        for i in range(1,len(prices)):
            sell[i] = max(buy[i-1]+prices[i], sell[i-1])
            buy[i] = max(sell[i-2]-prices[i], buy[i-1])

        print(sell)
        print(buy)
    
        return max(sell[-1], 0)
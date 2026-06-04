class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sell = [0] * len(prices)
        # buy = [0] * len(prices)
        # buy[0] = -prices[0]
        b = -prices[0]
        s = 0
        prev = 0


        for i in range(1,len(prices)):
            temp = s
            s, b = max(s, b+prices[i]), max(b, prev-prices[i])
            prev = temp
            # sell[i] = max(buy[i-1]+prices[i], sell[i-1])
            # buy[i] = max(sell[i-2]-prices[i], buy[i-1])

        # print(sell)
        # print(buy)
    
        return max(s, 0)
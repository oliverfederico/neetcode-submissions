class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l = 0
        r = len(prices) - 1
        lp_l = prices[l]
        rp_h = prices[r]
        profit = 0
        while l <= r:
            if prices[l] < lp_l:
                lp_l = prices[l]
            elif prices[l] > rp_h:
                profit = max(profit, prices[l] - lp_l)
            if prices[r] > rp_h: 
                rp_h = prices[r]
            elif prices[r] < lp_l:
                profit = max(profit, rp_h - prices[r])
            profit = max(profit, rp_h - lp_l)
            l+=1
            r-=1
        return profit



        
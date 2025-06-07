class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        if len(prices) == 1 or len(prices) == 0:
            return 0
        
        profit = []

        l = 0
        r = l+1

        while r < len(prices):

            profit.append(prices[r] - prices[l])
            if prices[r] < prices[l]:
                buy = prices[r]
                l+=1
            
            else:

        return max(profit)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache
        def dp(idx,buy,capacity):

            if idx >= len(prices):
                return 0
            if capacity <= 0:
                return 0
            not_transact = dp(idx+1,buy,capacity)
            transact = 0
            if buy:
                transact = -prices[idx] + dp(idx+1,False,capacity)
            else:
                transact = prices[idx] + dp(idx+1,True,capacity - 1)
            
            return max(transact,not_transact)
        
        return dp(0,True,2)


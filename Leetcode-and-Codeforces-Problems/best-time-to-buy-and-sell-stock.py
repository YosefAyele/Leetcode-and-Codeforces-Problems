class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = inf
        ans = 0
        for i,val in enumerate(prices):
            if val > min_:
                ans = max(ans,val - min_)
            else:
                min_ = min(min_, val)
                
        return ans
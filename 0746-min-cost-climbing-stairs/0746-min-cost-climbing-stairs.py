class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        
        top = len(cost)
     
        
        def dp(step):
            if step >= top:
                return 0
            if not memo[step]:
                memo[step]  = cost[step] + min(dp(step+1),dp(step+2))
            return memo[step]
        
        return min(dp(0),dp(1))
    
                
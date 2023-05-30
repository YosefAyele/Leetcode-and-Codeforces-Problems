class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        
        
        def dp(total):
            if total == amount:
                return 0
            if total > amount:
                return inf
            if total not in memo:
                curr = inf
                for coin in coins:
                    new_total = total + coin
                    curr = min(curr,dp(new_total) + 1)
                memo[total] = curr

            return memo[total]
                    
                    
            
        
        return dp(0) if dp(0) < inf else -1
        # print(memo)
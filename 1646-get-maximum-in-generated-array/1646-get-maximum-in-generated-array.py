class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n:
            return 0
        
        memo = {i:-1 for i in range(n + 1)}
        memo[0] = 0
        memo[1] = 1
        
        def dp(i):
            if i <= 1:
                return memo[i]
            if memo[i] == -1:
                if i%2:
                    memo[i] = dp(i//2) + dp(i//2 + 1)
                else:
                    memo[i] = dp(i//2)
            dp(i-1)

            return memo[i]
    
        dp(n)
      
        return max(memo.values())
        
        
    
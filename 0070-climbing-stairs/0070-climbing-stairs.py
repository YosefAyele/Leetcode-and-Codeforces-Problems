class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = defaultdict(int)
        memo[1] = 1
        memo[2] = 2
        def steps(n):
            if n < 3:
                return n
            if not memo[n]:
                memo[n] = steps(n-1) + steps(n-2)
            return memo[n]
        
        return steps(n)
    
                
                
            
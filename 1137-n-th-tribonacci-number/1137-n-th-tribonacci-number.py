class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        def dp(n):
            if n < 3:
                return memo[n]
            if not memo[n]:
                memo[n] = dp(n-1) + dp(n-2) + dp(n-3)
            return memo[n]
        return dp(n)
                
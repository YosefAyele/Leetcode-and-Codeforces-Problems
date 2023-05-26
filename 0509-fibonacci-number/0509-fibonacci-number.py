class Solution:
    def fib(self, n: int) -> int:
        
        memo = defaultdict(int)
        memo[0] = 0
        memo[1] = 1
        
        def fibo(n):
            if n <= 1:
                return n
            if memo[n]:
                return memo[n]
            memo[n] = fibo(n-1) + fibo(n-2)
            return memo[n]
        return fibo(n)
    
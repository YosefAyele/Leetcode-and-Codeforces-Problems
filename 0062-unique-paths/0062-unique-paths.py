class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        
        def isValid(i,j):
            if 0 <= i < m and 0 <= j < n:
                return dp[i][j]
            return 0
        
        dp[m-1][n-1] = 1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] += (isValid(i+1,j) + isValid(i,j+1))
                
        return dp[0][0]
    
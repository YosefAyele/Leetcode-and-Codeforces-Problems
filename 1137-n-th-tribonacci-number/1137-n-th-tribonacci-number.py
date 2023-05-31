class Solution:
    def tribonacci(self, n: int) -> int:
        x, y, z = 0, 1, 1
        
        if n == 0:
            return 0
        if n < 3:
            return 1
        
            
        for i in range(n-2):
            ans = x + y + z
            x = y
            y = z
            z = ans
        
        return ans
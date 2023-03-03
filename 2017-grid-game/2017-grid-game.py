class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        gridPrefix = [list(accumulate(row)) for row in grid]
        
        # print(gridPrefix)
        ans = float("inf")
        total1 = gridPrefix[0][-1]
        for i in range(len(grid[0])):
            
            right = total1 - gridPrefix[0][i]
            left = gridPrefix[1][i] - grid[1][i]
            
            curr = max(right,left)
            
            ans = min(ans,curr)
        
        return ans
        
            
            
            
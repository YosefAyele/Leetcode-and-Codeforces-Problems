class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        
        
        
        def dfs(r,c):
            grid[r][c] = 0
            ans = 1
            for x, y in directions:
                newR = r + x
                newC = c + y
                
                if inbound(newR,newC) and grid[newR][newC]:
                    ans += dfs(newR,newC)
                    
            return ans
        
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    
                    curr = dfs(row,col)
                    res = max(res,curr)
            
        return res
                    
                    
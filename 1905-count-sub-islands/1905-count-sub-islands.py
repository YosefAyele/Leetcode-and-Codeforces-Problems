class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        # do floodfill on the second then check out if it is also a land on the first one

        def inbound(r,c):
            return 0 <= r < len(grid1) and 0 <= c < len(grid1[0])
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def dfs(r,c):
            grid2[r][c] = 0
            
            nonlocal check
            
            if grid1[r][c] == 0:
                check = False
                
            for x,y in directions:
                newR = r + x
                newC = c + y
                
                if inbound(newR,newC) and grid2[newR][newC]:
                    dfs(newR,newC)
        
        res = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):

                if grid2[i][j] and grid1[i][j]:
                    
                    check = True
                    dfs(i,j)
                    if check:
                        res += 1
        
        return res
                    
                    
                    
                
            
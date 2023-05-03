class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        queue = deque()
        visited = set()
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        def dfs(node):
            visited.add(node)
            r,c = node
            queue.append((r,c,0))
            for x,y in directions:
                if inbound(r + x, c + y) and (r+x,c+y) not in visited and grid[r+x][c+y]:
                    dfs((r+x,c+y))
        flag = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    flag = True
                    dfs((row,col))
                    break
            if flag:
                break
        while queue:
            r,c,step = queue.popleft()
            
            for x,y in directions:
                r_ = r + x
                c_ = c + y
                
                if inbound(r_,c_) and (r_,c_) not in visited:
                    if grid[r_][c_] == 1:
                        return step
                    queue.append((r_,c_,step+1))
                    visited.add((r_,c_))
            

        
        
                    
                    
            
            
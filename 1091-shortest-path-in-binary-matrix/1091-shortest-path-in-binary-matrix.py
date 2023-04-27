class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < n
        
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        queue = deque()
        queue.append((0,0))
        
        
        path = 1
        while queue:
            length = len(queue)
            
            for _ in range(length):
                
                r, c = queue.popleft()
                if grid[r][c]==1:
                    continue
                grid[r][c] = 1
                
                
                if (r,c) == (n-1,n-1):
                    
                    return path 
                
                for x,y in directions:
                    next_row = r + x
                    next_col = c + y
                    
                    if inbound(next_row,next_col) and grid[next_row][next_col] == 0:
                        queue.append((next_row,next_col))
                        
            path += 1
        
        return -1
                        
                
        
        
        
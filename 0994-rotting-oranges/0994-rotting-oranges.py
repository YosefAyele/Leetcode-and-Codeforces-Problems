class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        
        
        queue = deque()
        fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    fresh += 1
        

        
        res = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue and fresh > 0:
            length = len(queue)
            
            for _ in range(length):
                r,c = queue.popleft()
                
                for x,y in directions:
                    if inbound(r + x, c + y) and grid[r + x][c + y] == 1:
                        grid[r + x][c + y] = 2
                        queue.append((r + x, c + y))
                        fresh -= 1
                        
            res += 1
   
        if fresh > 0:
            return -1
         
        return res
                
                
            
        
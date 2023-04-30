class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        n, m = len(maze), len(maze[0])
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m
        
        def isExit(r,c):
            return r == 0 or c == 0 or r == n-1 or c == m-1
        
        queue = deque()
        queue.append((entrance[0],entrance[1],0))
        visited = set((entrance[0],entrance[1]))
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            r, c, step = queue.popleft()
            
            if isExit(r,c) and (r,c) != tuple(entrance):
                return step
            for x,y in directions:
                R = r + x
                C = c + y
                
                if inbound(R,C) and (R,C) not in visited and maze[R][C] == ".":
                    queue.append((R,C,step + 1))
                    visited.add((R,C))
        
        return -1
            
         
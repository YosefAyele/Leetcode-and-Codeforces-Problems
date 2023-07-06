class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        m,n = len(grid),len(grid[0])
        def isValid(row,col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] != "#"
        k = 0
        queue = deque()
        visited  = defaultdict(set)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "@":
                    queue.append((r,c,0,0))
                    visited[0].add((r,c))
                if grid[r][c].islower():
                    k = k | (1 << (ord(grid[r][c]) - ord("a")))
        
        while queue:
            r,c,key,steps = queue.popleft()
            if key == k:
                return steps
            for x,y in directions:
                new_r = r + x
                new_c = c + y
                if isValid(new_r,new_c) and (new_r,new_c) not in visited[key]:
                    if grid[new_r][new_c].isupper():
                        if (1 << (ord(grid[new_r][new_c].lower()) - ord("a"))) & key:
                            queue.append((new_r,new_c,key,steps + 1))
                            
                            
                    elif  grid[new_r][new_c].islower():
                        newKey = key |  (1 << (ord(grid[new_r][new_c]) - ord("a")))
                        queue.append((new_r,new_c, newKey,steps + 1))
                        
                    else:
                        queue.append((new_r,new_c,key,steps + 1))
                    visited[key].add((new_r,new_c))
        return -1

                
        
                    
                    
                    
            
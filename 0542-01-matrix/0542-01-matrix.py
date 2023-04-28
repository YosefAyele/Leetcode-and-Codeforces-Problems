class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def inbound(r,c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])
        queue = deque()
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row,col,0))
        res = [[0]*len(mat[0]) for _ in range(len(mat))]
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set(queue)
        while queue:
            r,c,step = queue.popleft()
            res[r][c] = step
            for x,y in directions:
                R = r + x
                C = c + y
                
                if inbound(R,C) and mat[R][C] == 1 and (R,C) not in visited:
                    queue.append((R,C,step + 1))
                    visited.add((R,C))
                    
                    # mat[R][C] = 0
        
        return res
                    
                
                
        
        
        
        
        
        
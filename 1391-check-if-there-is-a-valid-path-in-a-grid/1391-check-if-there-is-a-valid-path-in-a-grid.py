class UnionFind:
    def __init__(self, row,col):
        self.root = {(i,j):(i,j) for i in range(row) for j in range(col)}
        self.rank = [[1]*col for _ in range(row)]

    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            
            rx,cx = rootX
            ry,cy = rootY
            if self.rank[rx][cx] > self.rank[ry][cy]:
                self.root[rootY] = rootX
                
            elif self.rank[rx][cx] < self.rank[ry][cy]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rx][cx] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        uf = UnionFind(len(grid),len(grid[0]))
        # print(uf.root) 
        def isvalid(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        directions = {1:[(0,-1),(0,1)], 2:[(1,0),(-1,0)], 3:[(0,-1),(1,0)], 4:[(0,1),(1,0)], 5:[(0,-1),(-1,0)], 6:[(0,1),(-1,0)]}
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                moves = directions[grid[i][j]]
                # print(moves)
                for x,y in moves:
                    r = i + x
                    c = j + y
                    
                    if isvalid(r,c):
                        moves_ = directions[grid[r][c]]
                        check = False
                        for x_, y_ in moves_:
                            if ( x == 0 and x_ == x and y == -y_) or (y == 0 and y == y_ and x == -x_):
                                check = True
                        if check:
                            uf.union((i,j),(r,c))
                        
                
        # print((0,0),(len(grid)-1,len(grid[0])-1))     
        # print(uf.root)
        
        return uf.connected((0,0),(len(grid)-1,len(grid[0])-1))
        
        
        
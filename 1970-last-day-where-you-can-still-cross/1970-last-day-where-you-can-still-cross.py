class UnionFind:
    def __init__(self, row,col):
        self.root ={(i,j):(i,j) for i in range(row) for j in range(col)}
        self.rank ={(i,j):1 for i in range(row) for j in range(col)}

    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        uf = UnionFind(row,col)
        
        directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        
        grid = [[0]*col for _ in range(row)]
        
      

        for x,y in cells:
            if y == 1:
                first = (x-1,y-1)
                break
        for x,y in cells:
            if y == col:
                last = (x-1,y-1)
                break
                
        
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        ans = 0
        for i in range(len(cells)):
            
            r,c = cells[i]
            # print(i,r,c)
            r -= 1
            c -= 1
            grid[r][c] = 1
            if c == 0:
                uf.union(first,(r,c))
            elif c == col - 1:
                uf.union(last,(r,c))
            for x,y in directions:
                r_ = r + x
                c_ = c + y
                
                if inbound(r_,c_) and grid[r_][c_] == 1:
                    uf.union((r,c),(r_,c_))
                    
            if uf.connected(first,last):
                return i
                    
            
            
                
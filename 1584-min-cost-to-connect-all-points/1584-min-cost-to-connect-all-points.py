# UnionFind class
class UnionFind:
    def __init__(self, points):
        self.root ={(i,j):(i,j) for i,j in points}
        self.rank ={(i,j):1 for i,j in points }

    
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # brute force approach
        uf = UnionFind(points)
        def manhatan(x1,x2,y1,y2):
            return abs(x1-x2) + abs(y1-y2)
        edges = []
        
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                cost = manhatan(x1,x2,y1,y2)
                
                edges.append([(x1,y1),(x2,y2),cost])
        edges.sort(key = lambda x:x[2])
        
        res = 0
        for p1,p2,cost in edges:
            if not uf.connected(p1,p2):
                uf.union(p1,p2)
                res += cost
        return res
                
                
  
                    
                    
        
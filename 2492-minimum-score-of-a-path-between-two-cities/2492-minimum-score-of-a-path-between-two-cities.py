class UnionFind:
    def __init__(self, size):
        self.root = {i+1:i+1 for i in range(size)}
        self.rank = {i+1:1 for i in range(size)}
            
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        for a,b,dist in roads:
            uf.union(a,b)
            
        res = inf
        for a,b,dist in roads:
            if uf.connected(a,1):
                res = min(res,dist)
                
        return res
        
            
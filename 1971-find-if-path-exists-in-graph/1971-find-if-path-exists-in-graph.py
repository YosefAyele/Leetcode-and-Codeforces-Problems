# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.rep = {i:i for i in range(size)}
        self.rank = [1]*size
    def representative(self, x):
        
        x = self.rep[x]
        
        while x != self.rep[x]:
            x = self.rep[x]
        
        return x
		
    def union(self, x, y):
        xrep = self.representative(x)
        yrep = self.representative(y)
        
        if self.rank[xrep] > self.rank[yrep]:
            self.rep[yrep] = xrep
            self.rank[xrep] += self.rank[yrep]
        else:
            self.rep[xrep] = yrep
            self.rank[yrep] += self.rank[xrep]     

    def connected(self, x, y):
        return self.representative(x) == self.representative(y)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        uf = UnionFind(n)
        
        for x,y in edges:
            uf.union(x,y)
        return uf.connected(source,destination)
    
class UnionFind:
    def __init__(self, coords):
        self.root = {(x,y):(x,y) for x,y in coords}
        
        self.rank = {(x,y):1 for x,y in coords}

    
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
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(stones)
        for i in range(len(stones)):
            for j in range(len(stones)):
                if i != j:
                    x1,y1 = stones[i]
                    x2,y2 = stones[j]
                    if x1 == x2 or y1 == y2:
                        uf.union((x1,y1),(x2,y2))
                        
        left = 0
        for x,y in stones:
            if uf.find((x,y)) == (x,y):
                # print(x,y)
                left += 1
        
        return len(stones) - left
        
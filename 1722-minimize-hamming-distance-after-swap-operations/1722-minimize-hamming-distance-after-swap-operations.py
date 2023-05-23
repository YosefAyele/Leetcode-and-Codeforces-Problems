class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    
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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = UnionFind(len(source))
        for a,b in allowedSwaps:
            uf.union(a,b)
        
        groups = defaultdict(dict)
        for i in range(len(source)):
            p = uf.find(i)
            groups[p][source[i]] = groups[p].get(source[i],0) + 1
            
        res = 0
        
        for i,val in enumerate(target):
            p = uf.find(i)
            
            if val not in groups[p]:
                res += 1
            else:
                groups[p][val] -= 1
                if groups[p][val] == 0:
                    groups[p].pop(val)
        return res
            
                
            
        
            
            
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        uf = UnionFind(len(s))
        for x,y in pairs:
            uf.union(x,y)
            
        groups = defaultdict(list)
        for i in range(len(s)):
            groups[uf.find(i)].append(i)
            
        
        for i in groups:
            group = groups[i]
            group.sort(key = lambda x:s[x],reverse = True)
            groups[i] = deque(group)
            
        res = []
        for idx in range(len(s)):
            p = uf.find(idx)
            res.append(s[groups[p].pop()])
        
        return "".join(res)
            
        
        
        
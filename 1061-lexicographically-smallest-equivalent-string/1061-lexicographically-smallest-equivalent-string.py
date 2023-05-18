class UnionFind:
    def __init__(self):
        self.root = {chr(97 + i):chr(97 + i) for i in range(27)}

    
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
            if rootY > rootX:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY


    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()

        for i in range(len(s1)):
            uf.union(s1[i],s2[i])
        res = []
        
        for s in baseStr:
            res.append(uf.find(s))
            
        return "".join(res)
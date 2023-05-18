# UnionFind class
class UnionFind:
    def __init__(self):
        self.root = {chr(97 + i):chr(97 + i) for i in range(27)}
        self.rank = {chr(97 + i):1 for i in range(27)}
        

    
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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        
        for string in equations:
            s1,eq1,eq2,s2 = list(string)
            
            if eq1 == eq2:
                uf.union(s1,s2)
        for string in equations:
            s1,eq1,eq2,s2 = list(string)
            if eq1 != eq2:
                if uf.connected(s1,s2):
                    return False
        return True
        
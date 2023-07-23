class UnionFind:
    def __init__(self,size):
        self.root = {i:i for i in range(size)}
        self.rank = {i:1 for i in range(size)}
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
    def connected(self,x,y):
        return self.find(x) == self.find(y)
                
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries_idx = [[i,queries[i]] for i in range(len(queries))]
        queries_idx.sort(key = lambda x: x[1][2])
        edgeList.sort(key = lambda x:x[2])
        
        # print(queries_idx)
        j = 0
        uf = UnionFind(n)
        res = [False]*len(queries)

        for i,query in queries_idx:
            p,q,limit = query

            while j < len(edgeList) and edgeList[j][2] < limit:
                x,y,_ = edgeList[j]
                uf.union(x,y)
                j += 1
            res[i] = uf.connected(p,q)
        return res


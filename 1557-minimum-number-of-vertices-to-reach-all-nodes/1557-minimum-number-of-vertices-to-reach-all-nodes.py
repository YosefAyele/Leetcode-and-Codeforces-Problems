class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        acceptors = defaultdict(int)
        
        for start,end in edges:
            acceptors[end] += 1
        
        res = set()
        for vertex1,vertex2 in edges:
            if  acceptors[vertex1] == 0:
                res.add(vertex1)
            if acceptors[vertex2] == 0:
                res.add(vertex2)
        
        return res
            
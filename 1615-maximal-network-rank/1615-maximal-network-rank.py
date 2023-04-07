class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        connections = defaultdict(set)
        
        for start, end in roads:
            connections[start].add(end)
            connections[end].add(start)
            
        
        
        res = 0
        for start in range(n):
            for end in range(n):
                if start != end:
                    if start in connections[end]:
                        curr = len(connections[start]) + len(connections[end]) - 1
                    else:
                        curr = len(connections[start]) + len(connections[end]) 
                    res = max(res,curr)
        
        return res
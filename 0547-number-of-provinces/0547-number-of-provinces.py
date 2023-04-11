class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        
        # first construct the adjacency list
        graph = defaultdict(list)
        
        for row in range(n):
            for col in range(n):
                if isConnected[row][col]:
                    graph[row].append(col)
        
        
        visited = set()
        def dfs(node):
            visited.add(node)
            
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child)
        res = 0
        for node in graph:
            if node not in visited:
                res += 1
                dfs(node)
        
        return res
                    
            
        
            
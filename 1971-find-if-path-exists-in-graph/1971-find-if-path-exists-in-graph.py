class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
        visited = set()
        
        def dfs(node):
            
            if node == destination:
                return True
            visited.add(node)
            
            for child in graph[node]:
                if child not in visited:
                    if dfs(child):
                        return True
                        
        return dfs(source)
                
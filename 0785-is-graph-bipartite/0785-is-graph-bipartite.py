class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1]*len(graph)
        
        def dfs(node,team):
            
            colors[node] = team
            
            for child in graph[node]:
                if colors[child] == -1:
                    if not dfs(child,1 - team):
                        return False
                elif colors[child] == team:
                        return False  
                       
            return True
            
        for node in range(len(graph)):
            if colors[node] == -1:
                if not dfs(node,1):
                    return False
                
        # print(colors) 
        return True
                
        
            
            
            
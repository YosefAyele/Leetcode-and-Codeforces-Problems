class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        
        for i in range(len(graph)):
            for num in graph[i]:
                adjList[i].append(num)
        
        paths = []
        
        def dfs(node,path):
            if node == len(graph) - 1:
                paths.append(path + [node])  
                return
            
            
            path.append(node)
            
            for child in adjList[node]:
                 dfs(child,path)
                    
            path.pop()
                    
        dfs(0,[])
        
        return paths
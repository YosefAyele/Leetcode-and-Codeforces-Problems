class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        colors = [0]*len(edges)
        graph = defaultdict(list)
        indegree = [0]*len(edges)
        for i in range(len(edges)):
            if edges[i] != -1:
                graph[i].append(edges[i])
                indegree[edges[i]] += 1
            
        
        
        def dfs(node,step):
            
            visited[node] = step
            colors[node] = -1
            for child in graph[node]:
                
                if colors[child] == -1:
                    if step - visited[child] + 1 >= 2:
                        colors[node] = 1
                        return step - visited[child] + 1
                    return -1
                if colors[child] == 0:
                    calls = dfs(child,step + 1)
                    if  calls != -1:
                        colors[node] = 1
                        return calls
            colors[node] = 1
            return -1
        res = -1
        for i in range(len(edges)):
            if edges[i] == -1:
                colors[i] = 1
                continue
            if colors[i] == 0:
                visited = defaultdict(int)
                size = dfs(i,0)
                if size != -1:
                    res = max(res,size)
        
        return res
                
        
            
            
        
        
        
                    

        
            
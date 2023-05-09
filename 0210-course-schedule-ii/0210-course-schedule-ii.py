class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # dfs approach
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        
        colors = [0]*numCourses
        
        # print(graph)
        res = []
        def dfs(node):
            if colors[node] == -1:
                return False
            
            colors[node] = -1
            
            for child in graph[node]:
                if colors[child] != 1:
                    if not dfs(child):
                        return False
                    
            colors[node] = 1
            res.append(node)
            
            return True
        for i in range(numCourses):
            if colors[i] == 0 :
                if not dfs(i):
                    return []
        
        return res[::-1]
        
                
            
            
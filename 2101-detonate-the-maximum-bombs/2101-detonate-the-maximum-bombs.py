class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def isInrange(bomb1,bomb2):
            x1,y1,r1 = bomb1
            x2,y2,r2 = bomb2
            return sqrt((x1 - x2)**2 + (y1 - y2)**2) <= r1
        
        graph = defaultdict(list)
        
        for i,bomb1 in enumerate(bombs):
            for j,bomb2 in enumerate(bombs):
                if isInrange(bomb1,bomb2):
                    graph[i].append(j)
        
        
        
        def dfs(node):
            
            visited.add(node)
            
            for child in graph[node]:
                if child not in visited:
                    dfs(child)
        res = 0
        for i in range(len(bombs)):
            visited = set()
            
            dfs(i)
            
            res = max(res,len(visited))
        
        return res
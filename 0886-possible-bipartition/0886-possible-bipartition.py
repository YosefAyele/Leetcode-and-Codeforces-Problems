class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        colors = [0]*n
        adjList = defaultdict(list)
        
        for a,b in dislikes:
            adjList[a].append(b)
            adjList[b].append(a)
        
        # print(adjList)
        
        def dfs(node,team):
            
            colors[node - 1] = team
            
            for child in adjList[node]:
                
                if colors[child - 1] != 0:
                    if colors[child - 1] == colors[node - 1]:
                        return False
                    
                else:
                    if not dfs(child,-team):
                        return False
    
            return True
        
        for i in range(n):
            if colors[i] == 0:
                if not dfs(i+1,1):
                    return False
        return True
                
                    
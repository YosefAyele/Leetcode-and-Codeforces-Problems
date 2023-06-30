class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        if len(parent) == 1:
            return 1
        for i,p in enumerate(parent):
            graph[p].append(i)
        
        ans = 0
        def dfs(node,parent):
            nonlocal ans
            if not graph[node]:
                if s[node] != parent:
                    return 1
                return 0
            
            max1 = 0
            max2 = 0
            
            for child in graph[node]:
                
                curr = dfs(child,s[node])
                if max1 < curr:
                    max2 = max1
                    max1 = curr
                elif max2 < curr:
                    max2 = curr
               
            ans = max(ans,max1 + max2+1)
            
            if s[node] != parent:
                return max(max1,max2) + 1
            else:
                return 0
        
        dfs(0,"-1")
        
        return ans

                
            
                
                    
            
            
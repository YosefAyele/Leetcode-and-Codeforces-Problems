class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        tree = defaultdict(list)
        
        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        def dfs(node,parent):
            
            if len(tree[node]) == 1 and tree[node][0] == parent:
                if hasApple[node]:
                    return True,1
                return False, 1
            edges = 0
            f_has = hasApple[node]
            for child in tree[node]:
                if child != parent:
                    has,n_edges = dfs(child,node)
                    if has:
                        edges += n_edges
                    f_has = f_has or has
            
            if f_has:
                return f_has,edges + 1
            return f_has,edges
        
        _,levels = dfs(0,-1)
        
        
        if levels:
            return (levels-1)*2
        return 0
                    
            
            
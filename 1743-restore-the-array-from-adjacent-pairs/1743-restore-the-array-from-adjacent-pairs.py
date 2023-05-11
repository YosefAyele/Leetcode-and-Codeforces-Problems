class Solution:
    def restoreArray(self, adj: List[List[int]]) -> List[int]:
        
        indegree = defaultdict(int)
        graph = defaultdict(list)
        
        for a,b in adj:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        queue = deque()
        for node in indegree:
            if indegree[node] == 1:
                queue.append((node,-1))
                break
        
        res = []
        while queue:
            node,parent = queue.popleft()
            res.append(node)
            for child in graph[node]:
                if child != parent:
                    indegree[child] -= 1
                    if indegree[child] <= 1:
                        queue.append((child,node))
        return res
                
                
            
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        indegree = [0]*n
        graph = defaultdict(list)
        
        
  
        for a,b in edges:
            graph[a].append(b)
            indegree[b] += 1
            
     
        queue = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        output = [set() for _ in range(n)]
        while queue:
            node = queue.popleft()
      
            for child in graph[node]:
                output[child].update(output[node])
                output[child].add(node)
                indegree[child] -= 1
                
                if not indegree[child]:
                    queue.append(child)
        
        output = [sorted(ancestors) for ancestors in output]
        
                
        return output
                
            
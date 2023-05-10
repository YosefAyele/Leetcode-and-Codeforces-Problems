class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        top = defaultdict(list)
        
        out = [0]*len(graph)
        for i in range(len(graph)):
            for node in graph[i]:
                top[node].append(i)
                out[i] += 1
        
        queue = deque()
        
        for i in range(len(graph)):
            if out[i] == 0:
                queue.append(i)
          
        res = []
        while queue:
            node = queue.popleft()
            
            res.append(node)
            
            for parent in top[node]:
                out[parent] -= 1
                if out[parent] == 0:
                    queue.append(parent)
        res.sort()
        return res
            
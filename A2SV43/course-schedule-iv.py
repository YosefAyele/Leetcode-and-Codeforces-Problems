class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0]*n
        
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
            
        queue = deque()
        ans = defaultdict(set)
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            
            for child in graph[node]:
                ans[child].add(node)
                ans[child].update(ans[node])
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        res = []
        for a,b in queries:
            res.append(b in ans[a])
        
        return res
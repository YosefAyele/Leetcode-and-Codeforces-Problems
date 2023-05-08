class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
            
        queue = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        res = []        
        while queue:
            node = queue.popleft()
            res.append(node)
            
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        if len(res) == numCourses:
            return res
        return []
                    
                    
            
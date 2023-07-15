class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def getPos(arr):
            graph = defaultdict(list)
            ans = defaultdict(lambda:-1)
            
            indegree = [0]*k
            for a,b in arr:
                graph[a].append(b)
                indegree[b - 1] += 1
            
            queue = deque()
            
            
            for idx,val in enumerate(indegree):
                
                if indegree[idx] == 0:
                    queue.append(idx+1)
            
            ans = []   
                    
            while queue:
                # print("trrr")
                node = queue.popleft()
                
                ans.append(node)
                
                for child in graph[node]:
                    indegree[child - 1] -= 1
                    if not indegree[child - 1]:
                        queue.append(child)
                        
            return ans
        rows = getPos(rowConditions)
        cols = getPos(colConditions)
        
        # print(rows,cols)
        res = [[0]*k for _ in range(k)]
        if len(rows) < k or len(cols) < k:
            return []
        
        for i,val in enumerate(rows):
            c = cols.index(val)
            res[i][c] = val
        return res
            
                
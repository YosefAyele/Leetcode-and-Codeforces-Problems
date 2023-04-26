class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
        
        res = [0]*n
        visited = set()
        def dfs(node):
            visited.add(node)
            if not graph[node]:
                curr = labels[node]
                idx = ord(curr) - 97
                
                arr = [0]*26
                arr[idx] = 1
                res[node] = 1
                return arr
            curr = [0]*26
            
            for child in graph[node]:
                if child not in visited:
                    newarr = dfs(child)
                    for i in range(26):
                        curr[i] += newarr[i]
                    
            curr[ord(labels[node])- 97] += 1
            res[node] = curr[ord(labels[node])- 97]
            return curr
        
        dfs(0)
        
        return res
            
                
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return [i for i in range(n)]
        #first build the graph
        graph = defaultdict(list)
        degree = [0]*n
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append((i,-1,0))
        '''
            My Guess: 
            the number of nodes with MHT are 2 and they are always adjacent
            run top sort and finally check the degree of each node, the ones which are 
            left with 1 degree are our answers
            
            now modified my idea
            - the nodes are still adjacent
            - the MH is starting from one of the nodes and end in either of the directions
            - nodes having one degree will be appended to the queue
            - the last two nodes which are added are our answers
        edge case:
             when the number of nodes are <= 2, here all the nodes can be possible answers
        '''
        
       
        res = deque()
        while queue:
            node,parent,step= queue.popleft()
            # print(node)
            if parent != -1:
                degree[parent] -= 1
            if len(res) > 2:
                res.popleft()
            if len(res) == 2 and res[0][1] < res[1][1]:
                res.popleft()
            
            for child in graph[node]:
                if child != parent:
                    # degree[node] -= 1
                    degree[child] -= 1
                    if degree[child] == 1:
                        res.append((child,step))
                        queue.append((child,node,step + 1))
                        
        return [x[0] for x in res]

                        
                        
            
                
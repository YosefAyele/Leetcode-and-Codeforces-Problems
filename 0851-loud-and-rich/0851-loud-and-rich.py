class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # first build the graph in a way that the neighbours are persons with more money than the node
        graph = defaultdict(list)
        
        for a,b in richer:
            graph[b].append(a)
        
        res = [501]*len(quiet)
        quiet_person = {quiet[i]:i for i in range(len(quiet))}
        visited = set()
        
        @cache
        def dfs(node):
            if not graph[node]:
                res[node] = node
                return quiet[node]
            # if res[node] != 501:
            #     return res[node]
            quietness = quiet[node]
            for child in graph[node]:
                quietness = min(quietness,dfs(child))
                
            res[node] = quiet_person[quietness]
            return quietness
        
        for i in range(len(quiet)):
            if res[i] == 501:
                dfs(i)
        
        return res
            
        